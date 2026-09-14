for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    func = "switchAdminTab" if "admin" in filename else "switchUserTab" if "user" in filename else "switchVolTab"

    # Replace the HTML calls
    text = text.replace(f'onclick="{func}(event, ', f'onclick="{func}(')
    
    # Make sure we add return false; to the end of the onclick if it's not already there
    # It currently looks like: onclick="switchAdminTab('tab-dashboard', this)"
    import re
    text = re.sub(r'onclick="' + func + r'\(\'(.*?)\', this\)"', f'onclick="{func}(\'\\1\', this); return false;"', text)

    # Replace the function definition
    text = text.replace(f'function {func}(event, tabId, el) {{', f'function {func}(tabId, el) {{')
    text = text.replace('if(event) event.preventDefault();\n', '')
    text = text.replace('if(event) event.preventDefault();', '')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Brute forced event removal.")
