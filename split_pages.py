import os
import re

def create_pages(base_file, tabs_config):
    with open(base_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the main tabs container
    # We will just extract all the .admin-tab or .vol-tab or .user-tab divs
    tab_class = "admin-tab" if "admin" in base_file else "user-tab" if "user" in base_file else "vol-tab"
    
    # We need to replace the JS links with actual HTML links!
    # E.g. href="#" class="tab-link active" onclick="switchAdminTab('tab-dashboard', this); return false;"
    # becomes href="admin.html" class="tab-link"
    
    for current_tab_id, current_filename in tabs_config.items():
        new_html = html
        
        # 1. Update the links to point to the new files
        for target_tab_id, target_filename in tabs_config.items():
            # If this is the current page, make it active
            active_str = 'active' if target_tab_id == current_tab_id else ''
            
            # Replace the link in the HTML
            # The link looks like: <a href="#" class="tab-link active" onclick="switchAdminTab('tab-requests', this); return false;">
            # Or some variation. Let's use a robust regex.
            pattern = r'<a href="#" class="tab-link(?: active)?" onclick="switch[a-zA-Z]+\(\'' + target_tab_id + r'\', this\); return false;">'
            replacement = f'<a href="{target_filename}" class="tab-link {active_str}">'
            new_html = re.sub(pattern, replacement, new_html)
            
        # 2. Hide all tabs except the current one
        for target_tab_id, target_filename in tabs_config.items():
            if target_tab_id == current_tab_id:
                # Make it visible
                new_html = re.sub(r'<div id="' + target_tab_id + r'" class="' + tab_class + r'" style="display: none;">', f'<div id="{target_tab_id}" class="{tab_class}">', new_html)
            else:
                # Make it hidden (or remove it entirely, but hiding is safer so we don't break CSS)
                # First ensure it has display:none if it doesn't already
                if f'<div id="{target_tab_id}" class="{tab_class}">' in new_html:
                    new_html = new_html.replace(f'<div id="{target_tab_id}" class="{tab_class}">', f'<div id="{target_tab_id}" class="{tab_class}" style="display: none;">')

        # 3. Remove the switchTab function completely from this new file so it doesn't cause errors
        new_html = re.sub(r'function switch[a-zA-Z]+\(tabId, el\) \{.*?\n        \}', '', new_html, flags=re.DOTALL)
        
        # Write the new file
        with open(f"templates/{current_filename}", 'w', encoding='utf-8') as f:
            f.write(new_html)

admin_tabs = {
    'tab-dashboard': 'admin.html',
    'tab-requests': 'admin-requests.html',
    'tab-reports': 'admin-reports.html',
    'tab-volunteers': 'admin-volunteers.html',
    'tab-directory': 'admin-directory.html',
    'tab-settings': 'admin-settings.html'
}
create_pages('templates/admin.html', admin_tabs)

user_tabs = {
    'tab-active': 'user-dashboard.html',
    'tab-history': 'user-history.html'
}
create_pages('templates/user-dashboard.html', user_tabs)

vol_tabs = {
    'tab-nearby': 'volunteer-dashboard.html',
    'tab-certificate': 'volunteer-certificate.html'
}
create_pages('templates/volunteer-dashboard.html', vol_tabs)

print("Split all dashboards into native HTML pages.")
