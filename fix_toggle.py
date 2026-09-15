import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix button text completely
js = re.sub(r'<span id="lang-text">[^<]*</span>', r'<span id="lang-text">${currentLang === \'en\' ? \'मराठी\' : \'English\'}</span>', js)

# Fix toggle click event
new_toggle = '''        langToggleBtn.addEventListener('click', () => {
            if (currentLang === 'en') {
                currentLang = 'mr';
            } else {
                currentLang = 'en';
            }
            localStorage.setItem('able_lang', currentLang);
            
            // Force reload to apply clean state, applyTranslations sometimes struggles with dynamic DOM
            window.location.reload();
        });'''

js = re.sub(r'        langToggleBtn\.addEventListener\(\'click\', \(\) => \{.*?        \}\);', new_toggle, js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed toggle!')
