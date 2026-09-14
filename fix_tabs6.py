import re

for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    func = "switchAdminTab" if "admin" in filename else "switchUserTab" if "user" in filename else "switchVolTab"

    # Replace <a href="#" class="tab-link..." onclick="func(event, 'tab', this)">
    # with <a href="#" class="tab-link..." onclick="func('tab', this); return false;">
    
    def replacer(match):
        active = match.group(1) or ""
        tab = match.group(2)
        return f'href="#" class="tab-link {active}" onclick="{func}(\'{tab}\', this); return false;"'

    text = re.sub(r'href="#" class="tab-link (active )?" onclick="' + func + r'\(event, \'(.*?)\', this\)"', replacer, text)

    # Now update the function definition to remove 'event'
    text = text.replace(f'function {func}(event, tabId, el) {{', f'function {func}(tabId, el) {{')
    text = text.replace('if(event) event.preventDefault();\n', '')
    text = text.replace('if(event) event.preventDefault();', '')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Removed event parameter and added return false.")
