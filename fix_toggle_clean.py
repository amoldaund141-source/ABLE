import re
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Completely replace the language toggle button injection with perfectly formatted JS
clean_btn = """      // Inject Language Toggle Button into the header
      const navContainer = document.querySelector('.nav-container');
      if (navContainer) {
          navContainer.insertAdjacentHTML('beforeend', `
              <button id="lang-toggle" class="btn secondary" style="padding: 6px 10px; margin-left: 10px; font-size: 0.9rem;">
                  <span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.1rem; margin-right: 4px;">translate</span> 
                  <span id="lang-text">${currentLang === 'en' ? 'मराठी' : 'English'}</span>
              </button>
          `);
      }"""

# Use regex to strip out the old block (from // Inject Language... to the closing brace of the if block)
js = re.sub(r'// Inject Language Toggle Button into the header.*?\}\s+', clean_btn + '\n\n', js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Replaced lang-toggle block!")
