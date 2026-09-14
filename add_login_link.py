import glob
import re

files = glob.glob('*.html')
# don't touch dashboards or login since they have their own navs
skip_files = ['login.html', 'admin.html', 'volunteer-dashboard.html', 'user-dashboard.html']

for filepath in files:
    if filepath in skip_files:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Login is already in the nav
    if 'href="login.html"' not in content:
        # Find </ul> inside <nav> and insert the login link right before it
        login_link = '\n                    <li><a href="login.html" style="color: var(--brand-blue); font-weight: 700;"><span class="material-symbols-outlined" style="vertical-align: middle;">login</span> Login</a></li>\n                '
        
        # Replace the first instance of </ul> after <nav
        # Or just replace the </ul> inside the nav.
        
        # We can just do a regex replace for the specific block
        content = re.sub(r'(<li><a href="report.html">Report</a></li>\s*)</ul>', 
                         r'\1' + login_link + '</ul>', 
                         content)
                         
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Login link added to all public pages.")
