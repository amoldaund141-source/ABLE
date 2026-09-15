import glob

old_btn = '''<button class="btn" onclick="showNotification('New Report', 'Opening barrier submission form...', 'add', '#2563eb')"><span class="material-symbols-outlined" style="margin-right: 8px;">add</span> New Report</button>'''
new_btn = '''<button class="btn" onclick="window.location.href='report.html'"><span class="material-symbols-outlined" style="margin-right: 8px;">add</span> New Report</button>'''

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(old_btn, new_btn)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print('Updated New Report button!')
