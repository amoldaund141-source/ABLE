import os
import re
import glob

files = glob.glob('templates/admin*.html')

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add "Directory" and "Settings" to the top navbar (before Logout)
    # The top navbar looks like:
    # <li><a href="admin-reports.html" ...>... Reports</a></li>
    # <li><a href="index.html" style="color: #ef4444;" ...>... Logout</a></li>
    
    # Let's find the Logout link and insert Directory and Settings before it
    directory_link = '<li><a href="admin-directory.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.2rem; margin-right: 4px;">place</span> Directory</a></li>\n                    '
    settings_link = '<li><a href="admin-settings.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.2rem; margin-right: 4px;">settings</span> Settings</a></li>\n                    '
    
    # Fix active state for directory and settings if we are on those pages
    if 'directory' in filename:
        directory_link = directory_link.replace('tab-link "', 'tab-link active"')
    if 'settings' in filename:
        settings_link = settings_link.replace('tab-link "', 'tab-link active"')
        
    logout_pattern = r'(<li><a href="index.html" style="color: #ef4444;".*?Logout</a></li>)'
    
    # Only insert if they aren't already there
    if 'Directory</a></li>' not in html:
        html = re.sub(logout_pattern, directory_link + settings_link + r'\1', html)

    # 2. Delete the vertical sidebar completely
    # The sidebar is:
    # <aside class="sidebar"> ... </aside>
    html = re.sub(r'\s*<aside class="sidebar">.*?</aside>', '', html, flags=re.DOTALL)
    
    # 3. Fix the grid layout so it doesn't leave a massive empty space where the sidebar was
    # The layout is: <div class="dashboard-grid">
    # CSS: .dashboard-grid { display: grid; grid-template-columns: 250px 1fr; gap: 30px; margin-top: 40px; }
    # Let's change grid-template-columns to 1fr!
    html = html.replace('grid-template-columns: 250px 1fr;', 'grid-template-columns: 1fr;')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Moved all links to the horizontal top navbar and deleted the vertical sidebar.")
