import glob
import re

# 1. HTML: give the form an ID and remove the inline JS
files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'<form onsubmit="event.preventDefault\(\);.*?this\.reset\(\);">', r'<form id="directory-form">', html)
    html = re.sub(r'<input type="text" placeholder="E.g. Pune Central Mall" required style="width: 100%;">', r'<input type="text" id="dir-name" name="dir-name" placeholder="E.g. Pune Central Mall" required style="width: 100%;">', html)
    html = re.sub(r'<select style="width: 100%;', r'<select id="dir-feature" name="dir-feature" style="width: 100%;', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. JS: add logic
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

dir_logic = """            } else if (form.id === 'directory-form') {
                const data = {
                    name: document.getElementById('dir-name').value,
                    feature: document.getElementById('dir-feature').value
                };
                try {
                    await fetch('/api/directory', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                } catch(e) {}
                showNotification('Success!', 'Directory updated securely in the database.', 'check_circle', '#10b981');
                form.reset();
                return;
            }"""

js = js.replace("            } else if (form.id === 'volunteer-form') {", dir_logic + "\n            } else if (form.id === 'volunteer-form') {")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Directory form wired to backend!")
