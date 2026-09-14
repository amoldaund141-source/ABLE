import re

for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    func = "switchAdminTab" if "admin" in filename else "switchUserTab" if "user" in filename else "switchVolTab"

    # Replace <a class="tab-link..." onclick="func('tab', this)" ...>
    # with <a href="#" class="tab-link..." onclick="func(event, 'tab', this)">
    def replacer(match):
        active = match.group(1) or ""
        tab = match.group(2)
        return f'href="#" class="tab-link {active}" onclick="{func}(event, \'{tab}\', this)"'

    text = re.sub(r'class="tab-link (active )?" onclick="' + func + r'\(\'(.*?)\', this\)" style="cursor:pointer;"', replacer, text)

    # Now update the function definition
    text = text.replace(f'function {func}(tabId, el) {{', f'function {func}(event, tabId, el) {{\n            if(event) event.preventDefault();\n            console.log("Switching to tab: " + tabId);')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Restored href='#' and event.preventDefault()")
