import re

with open('templates/admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the DOMContentLoaded block
text = re.sub(r'\s*// Attach click listeners to all tab links.*?\}\);\s*', '\n\n', text, flags=re.DOTALL)

# Add onclick handlers back
def replacer(match):
    active = match.group(1) or ""
    tab = match.group(2)
    return f'class="tab-link {active}" onclick="switchAdminTab(\'{tab}\', this)" style="cursor:pointer;"'

text = re.sub(r'class="tab-link (active )?" data-tab="(.*?)" style="cursor:pointer;"', replacer, text)

with open('templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done fixing admin.html')
