import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the syntax error: remove the extra closing brace
js = js.replace("            }\n            } else if (form.id === 'volunteer-form') {", "            } else if (form.id === 'volunteer-form') {")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Syntax error fixed!")
