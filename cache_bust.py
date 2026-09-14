import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the old script tag with a cache-busted one
    content = content.replace('<script src="script.js"></script>', '<script src="script.js?v=2"></script>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cache busted in all HTML files.")
