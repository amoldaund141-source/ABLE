import glob
import re

# 1. Update admin-requests.html
with open('templates/admin-requests.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<tbody>', '<tbody id="admin-requests-tbody">')
with open('templates/admin-requests.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update admin-reports.html
with open('templates/admin-reports.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<tbody>', '<tbody id="admin-reports-tbody">')
with open('templates/admin-reports.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update user-dashboard.html
with open('templates/user-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<tbody>', '<tbody id="user-requests-tbody">')
with open('templates/user-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added IDs to tbodys!")
