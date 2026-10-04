import re

with open('static/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add UI UX Pro Max overrides for touch targets at the end of the file
touch_css = """

/* UI UX Pro Max Skill Enhancements - Touch Targets */
button, 
.btn, 
input[type="text"], 
input[type="password"], 
input[type="email"], 
select, 
textarea {
    min-height: 44px; /* Strict iOS/Mobile Touch Target Minimum */
}
"""
css += touch_css

with open('static/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Enhance accessibility of the mock modal
target_modal = '<div class="mock-modal" id="form-modal">'
replacement_modal = '<div class="mock-modal" id="form-modal" role="alertdialog" aria-modal="true" aria-live="assertive">'
js = js.replace(target_modal, replacement_modal)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("UI UX Pro Max guidelines safely applied!")
