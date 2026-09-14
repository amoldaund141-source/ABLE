import os
import glob

html_files = glob.glob('*.html')

# The CDN link for Material Icons
icon_link = '\n    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">\n'

# The Dark mode toggle button
theme_btn = '<button id="theme-toggle" class="btn secondary" style="padding: 8px 12px; margin-left: 15px;"><span class="material-symbols-outlined">dark_mode</span></button>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add icon link if not present
    if 'Material+Symbols' not in content:
        content = content.replace('</head>', f'{icon_link}</head>')
    
    # Add theme toggle button into nav if not present
    if 'theme-toggle' not in content:
        content = content.replace('</nav>', f'</nav>\n            {theme_btn}')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files upgraded.")
