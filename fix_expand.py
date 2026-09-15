with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("querySelectorAll('a, button, h1, h2, h3, th')", "querySelectorAll('a, button, h1, h2, h3, h4, th, td, p, span, div, strong, label, option')")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Expanded translations to all elements!')
