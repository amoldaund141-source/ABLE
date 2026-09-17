with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace \' with ' inside the template literal
js = js.replace("\\'en\\'", "'en'")
js = js.replace("\\'मराठी\\'", "'मराठी'")
js = js.replace("\\'English\\'", "'English'")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed syntax error!')
