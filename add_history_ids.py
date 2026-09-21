import glob
import re

# 1. user-history.html
with open('templates/user-history.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<tbody>(.*?)</tbody>', r'<tbody id="user-history-tbody"></tbody>', html, flags=re.DOTALL)
with open('templates/user-history.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. volunteer-history.html
with open('templates/volunteer-history.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<tbody>(.*?)</tbody>', r'<tbody id="volunteer-history-tbody"></tbody>', html, flags=re.DOTALL)
with open('templates/volunteer-history.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected history table IDs!")
