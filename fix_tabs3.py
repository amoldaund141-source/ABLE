import re

for filename in ['templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'\s*// Attach click listeners to all tab links.*?\}\);\s*', '\n\n', text, flags=re.DOTALL)

    func = "switchUserTab" if "user" in filename else "switchVolTab"

    def replacer(match):
        active = match.group(1) or ""
        tab = match.group(2)
        return f'class="tab-link {active}" onclick="{func}(\'{tab}\', this)" style="cursor:pointer;"'

    text = re.sub(r'class="tab-link (active )?" data-tab="(.*?)" style="cursor:pointer;"', replacer, text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print('Done fixing other dashboards')
