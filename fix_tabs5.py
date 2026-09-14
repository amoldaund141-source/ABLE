import re

for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    func = "switchAdminTab" if "admin" in filename else "switchUserTab" if "user" in filename else "switchVolTab"

    # Replace <a class="tab-link..." data-tab="..." style="...">
    # with <a href="#" class="tab-link..." onclick="func(event, 'tab', this)">
    def replacer(match):
        active = match.group(1) or ""
        tab = match.group(2)
        return f'href="#" class="tab-link {active}" onclick="{func}(event, \'{tab}\', this)"'

    # The current string in the file looks like: class="tab-link" data-tab="tab-requests" style="cursor:pointer;"
    text = re.sub(r'class="tab-link (active )?" data-tab="(.*?)" style="cursor:pointer;"', replacer, text)

    # Now let's fix the DOMContentLoaded event listener block if it exists
    text = re.sub(r'\s*// Attach click listeners to all tab links.*?\(\);\s*', '\n', text, flags=re.DOTALL)
    text = re.sub(r'\s*// Attach click listeners to all tab links.*?\}\);\s*', '\n', text, flags=re.DOTALL)

    # Make sure switchAdminTab signature is correct
    # It might be function switchAdminTab(event, tabId, el) { or function switchAdminTab(tabId, el) {
    # Let's normalize it
    text = re.sub(r'function ' + func + r'\(.*?\)\s*\{', f'function {func}(event, tabId, el) {{', text)
    
    # Ensure preventDefault is there
    if 'event.preventDefault()' not in text:
        text = text.replace(f'function {func}(event, tabId, el) {{', f'function {func}(event, tabId, el) {{\n            if(event) event.preventDefault();')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("COMPLETELY fixed all tabs logic.")
