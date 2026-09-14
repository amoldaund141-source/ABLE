import glob

files = glob.glob('*.html')

head_injection = """
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#2563eb">
"""

script_injection = """
    <script>
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('sw.js').then(reg => {
            console.log('ServiceWorker registration successful');
          }).catch(err => {
            console.log('ServiceWorker registration failed: ', err);
          });
        });
      }
    </script>
</body>
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="manifest"' not in content:
        content = content.replace('</head>', head_injection + '</head>')
        
    if 'serviceWorker' not in content:
        content = content.replace('</body>', script_injection)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("PWA features injected into all HTML files.")
