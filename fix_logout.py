import glob

# 1. Update static/script.js
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("localStorage.clear()", "localStorage.removeItem('able_logged_in'); localStorage.removeItem('able_role')")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)


# 2. Update all HTML files that have the logout() function
files = glob.glob('templates/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace("localStorage.clear();", "localStorage.removeItem('able_logged_in');\\n            localStorage.removeItem('able_role');")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed logout clearing preferences!")
