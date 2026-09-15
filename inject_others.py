import re

files = ['templates/volunteer-dashboard.html', 'templates/volunteer-history.html', 'templates/volunteer-certificate.html']
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    nearby = '<li><a href="volunteer-dashboard.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">map</span> Nearby Requests</a></li>\n                    '
    history = '<li><a href="volunteer-history.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">history</span> My History</a></li>\n                    '
    cert = '<li><a href="volunteer-certificate.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">workspace_premium</span> Certificate</a></li>\n                    '
    
    if 'dashboard' in filename: nearby = nearby.replace('tab-link "', 'tab-link active"')
    if 'history' in filename: history = history.replace('tab-link "', 'tab-link active"')
    if 'certificate' in filename: cert = cert.replace('tab-link "', 'tab-link active"')

    if 'Nearby Requests</a></li>' not in html:
        html = html.replace('<li><a href="#" onclick="logout()"', nearby + history + cert + '<li><a href="#" onclick="logout()"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

files = ['templates/user-dashboard.html', 'templates/user-history.html']
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    active = '<li><a href="user-dashboard.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">pending_actions</span> Active Requests</a></li>\n                    '
    history = '<li><a href="user-history.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 4px;">history</span> Past Requests</a></li>\n                    '
    
    if 'dashboard' in filename: active = active.replace('tab-link "', 'tab-link active"')
    if 'history' in filename: history = history.replace('tab-link "', 'tab-link active"')

    if 'Active Requests</a></li>' not in html:
        html = html.replace('<li><a href="#" onclick="logout()"', active + history + '<li><a href="#" onclick="logout()"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Injected correctly using simple string replace.")
