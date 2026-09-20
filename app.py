import os
import sqlite3
from flask import Flask, request, jsonify, render_template
import datetime

# Separate frontend (templates/static) and backend (app.py)
app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY, email TEXT, location TEXT, req_type TEXT, status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, email TEXT, location TEXT, issue TEXT, severity TEXT, status TEXT, date TEXT)''')
    
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (email, password, role) VALUES ('admin@able.org', 'admin123', 'admin')")
        c.execute("INSERT INTO users (email, password, role) VALUES ('volunteer@nss.org', 'vol123', 'volunteer')")
        c.execute("INSERT INTO users (email, password, role) VALUES ('user@citizen.org', 'user123', 'user')")
        c.execute("INSERT INTO requests (email, location, req_type, status) VALUES ('user@citizen.org', 'Pune Station, Platform 1', 'Mobility (Wheelchair)', 'Pending')")
        c.execute("INSERT INTO requests (email, location, req_type, status) VALUES ('other@citizen.org', 'Modern College Main Gate', 'Navigation Guide', 'Dispatched')")
    
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- HTML SERVING ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page_name>.html')
def serve_html_pages(page_name):
    return render_template(f'{page_name}.html')

# --- API ROUTES ---
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (data.get('email'), data.get('password'))).fetchone()
    conn.close()
    
    if user:
        return jsonify({"success": True, "role": user['role']})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route('/api/requests', methods=['GET', 'POST'])
def handle_requests():
    conn = get_db()
    if request.method == 'POST':
        data = request.json
        conn.execute("INSERT INTO requests (email, location, req_type, status) VALUES (?, ?, ?, 'Pending')", 
                     (data.get('email', 'anonymous'), data.get('location'), data.get('req_type')))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Request saved to database."})
    
    # GET
    reqs = conn.execute("SELECT * FROM requests ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in reqs])

@app.route('/api/reports', methods=['GET', 'POST'])
def handle_reports():
    conn = get_db()
    if request.method == 'POST':
        data = request.json
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        conn.execute("INSERT INTO reports (email, location, issue, severity, status, date) VALUES (?, ?, ?, ?, 'Investigating', ?)", 
                     (data.get('email', 'anonymous'), data.get('location'), data.get('issue'), data.get('severity', 'Medium'), date_str))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Report saved to database."})
    
    # GET
    reps = conn.execute("SELECT * FROM reports ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in reps])

@app.route('/api/requests/<int:req_id>/accept', methods=['POST'])
def accept_request(req_id):
    conn = get_db()
    conn.execute("UPDATE requests SET status='Dispatched' WHERE id=?", (req_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Request accepted and dispatched."})

if __name__ == '__main__':
    print("Starting ABLE Backend Server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
