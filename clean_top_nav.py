import re
import glob

files = glob.glob('templates/admin*.html')

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to remove the specific li tags containing Dashboard, All Requests, Volunteers, and Reports
    # from the admin-top-nav.
    
    html = re.sub(r'\s*<li><a href="admin.*?Dashboard</a></li>', '', html)
    html = re.sub(r'\s*<li><a href="admin.*?All Requests</a></li>', '', html)
    html = re.sub(r'\s*<li><a href="admin.*?Volunteers</a></li>', '', html)
    html = re.sub(r'\s*<li><a href="admin.*?Reports</a></li>', '', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Cleaned top navbar in {len(files)} admin files.")
