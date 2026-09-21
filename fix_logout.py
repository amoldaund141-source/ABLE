import glob
import re

# 1. Update script.js to add a robust logout function and fix injection
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

logout_func = """
// --- Robust Logout ---
window.logoutUser = function(e) {
    if (e) e.preventDefault();
    localStorage.removeItem('able_logged_in');
    localStorage.removeItem('able_role');
    localStorage.removeItem('able_email');
    window.location.replace('index.html');
};
"""
js = logout_func + js

# Replace all inline onclicks with the robust function in the injection
js = re.sub(r'onclick="localStorage\.removeItem\(\'able_logged_in\'\); localStorage\.removeItem\(\'able_role\'\); window\.location\.href=\'index\.html\';"', 'onclick="logoutUser(event)"', js)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Update all hardcoded HTML files to ensure they also call the function just in case
files = glob.glob('templates/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Target any a tag with href="index.html" that has "Logout" in it
    # We will just replace it if it's the exact string used in admin/volunteer pages
    pattern1 = r'<a href="index\.html" style="color: #ef4444;"><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1\.2rem; margin-right: 4px;">logout</span> Logout</a>'
    replacement1 = r'<a href="#" onclick="logoutUser(event)" style="color: #ef4444;"><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.2rem; margin-right: 4px;">logout</span> Logout</a>'
    
    pattern2 = r'<a href="index\.html"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a>'
    replacement2 = r'<a href="#" onclick="logoutUser(event)"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a>'
    
    html = re.sub(pattern1, replacement1, html)
    html = re.sub(pattern2, replacement2, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Logout buttons fully fortified!")
