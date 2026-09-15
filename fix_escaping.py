import glob

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace("showNotification(\\'Barrier", "showNotification('Barrier")
    html = html.replace("\\', `", "', `")
    html = html.replace("`, \\'visibility\\', \\'#3b82f6\\')", "`, 'visibility', '#3b82f6')")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print('Fixed escaping!')
