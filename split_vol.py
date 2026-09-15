import shutil, glob, re

# 1. Create volunteer-requests.html by copying volunteer-dashboard.html
shutil.copy('templates/volunteer-dashboard.html', 'templates/volunteer-requests.html')

# 2. Modify volunteer-dashboard.html to show a new 'tab-dashboard'
dashboard_content = '''
                <div id="tab-dashboard" class="vol-tab">
                    <h2 style="margin-bottom: 20px;">Volunteer Overview</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px;">
                        <div class="card" style="text-align: center;">
                            <span class="material-symbols-outlined" style="font-size: 3rem; color: #2563eb; margin-bottom: 10px;">volunteer_activism</span>
                            <h3 style="font-size: 2rem;">14</h3>
                            <p style="color: var(--text-muted);">Citizens Helped</p>
                        </div>
                        <div class="card" style="text-align: center;">
                            <span class="material-symbols-outlined" style="font-size: 3rem; color: #10b981; margin-bottom: 10px;">schedule</span>
                            <h3 style="font-size: 2rem;">22</h3>
                            <p style="color: var(--text-muted);">Hours Logged</p>
                        </div>
                        <div class="card" style="text-align: center;">
                            <span class="material-symbols-outlined" style="font-size: 3rem; color: #f59e0b; margin-bottom: 10px;">military_tech</span>
                            <h3 style="font-size: 2rem;">Gold</h3>
                            <p style="color: var(--text-muted);">Current Rank</p>
                        </div>
                    </div>
                    
                    <div class="card">
                        <h3 style="margin-bottom: 15px;">Next Assigned Shift</h3>
                        <p style="margin-bottom: 8px;"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 8px;">calendar_month</span> <strong>Date:</strong> Tomorrow, 10:00 AM - 2:00 PM</p>
                        <p style="margin-bottom: 8px;"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 8px;">location_on</span> <strong>Location:</strong> Pune Railway Station</p>
                        <p style="margin-bottom: 8px;"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 8px;">badge</span> <strong>Role:</strong> General Mobility Assistant</p>
                    </div>
                </div>
'''

with open('templates/volunteer-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace tab-nearby with the new dashboard_content in volunteer-dashboard.html
html = re.sub(r'<div id="tab-nearby" class="vol-tab">.*?</div>\s*</div>', dashboard_content, html, flags=re.DOTALL)
with open('templates/volunteer-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update the hardcoded navbars in all volunteer-*.html files to include both links
# We will use re.sub on the <ul id="main-nav"> block
nav_html = '''<ul id="main-nav">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="volunteer-dashboard.html" class="tab-link {dash_active}"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">dashboard</span> My Dashboard</a></li>
                    <li><a href="volunteer-requests.html" class="tab-link {req_active}"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">map</span> Nearby Requests</a></li>
                    <li><a href="volunteer-history.html" class="tab-link {hist_active}"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">history</span> My History</a></li>
                    <li><a href="volunteer-certificate.html" class="tab-link {cert_active}"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">workspace_premium</span> Certificate</a></li>
                    <li><a href="#" onclick="logout()" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
                </ul>'''

files = glob.glob('templates/volunteer-*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    dash_active = 'active' if 'dashboard' in file else ''
    req_active = 'active' if 'requests' in file else ''
    hist_active = 'active' if 'history' in file else ''
    cert_active = 'active' if 'certificate' in file else ''
    
    this_nav = nav_html.format(dash_active=dash_active, req_active=req_active, hist_active=hist_active, cert_active=cert_active)
    html = re.sub(r'<ul id="main-nav">.*?</ul>', this_nav, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 4. Update script.js to point Nearby Requests to volunteer-requests.html
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('<li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Nearby Requests</a></li>', '<li><a href="volunteer-requests.html"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Nearby Requests</a></li>')
with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Split volunteer dashboard successfully!")
