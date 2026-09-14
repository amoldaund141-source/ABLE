import glob, re
files = glob.glob('templates/admin*.html')
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f: html = f.read()
    
    dir_link = '<li><a href="admin-directory.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.2rem; margin-right: 4px;">place</span> Directory</a></li>\n                    '
    set_link = '<li><a href="admin-settings.html" class="tab-link "><span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.2rem; margin-right: 4px;">settings</span> Settings</a></li>\n                    '
    
    if 'directory' in filename: dir_link = dir_link.replace('tab-link "', 'tab-link active"')
    if 'settings' in filename: set_link = set_link.replace('tab-link "', 'tab-link active"')
    
    if 'Directory</a></li>' not in html:
        html = re.sub(r'(<li><a href="index\.html" style="color: #ef4444;".*?Logout</a></li>)', dir_link + set_link + r'\1', html)
        with open(filename, 'w', encoding='utf-8') as f: f.write(html)
print('Done injecting Directory and Settings into top navbar')
