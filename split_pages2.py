import os
import re

def create_pages(base_file, tabs_config):
    with open(base_file, 'r', encoding='utf-8') as f:
        html = f.read()

    tab_class = "admin-tab" if "admin" in base_file else "user-tab" if "user" in base_file else "vol-tab"
    
    for current_tab_id, current_filename in tabs_config.items():
        new_html = html
        
        for target_tab_id, target_filename in tabs_config.items():
            active_str = 'active' if target_tab_id == current_tab_id else ''
            
            # This regex matches BOTH the new native links (if we run it on an already split file)
            # AND the old JS links
            pattern_js = r'<a href="#" class="tab-link(?: active)?" onclick="switch[a-zA-Z]+\(\'' + target_tab_id + r'\', this\); return false;">'
            pattern_html = r'<a href=".*?" class="tab-link(?: active)?">(.*?)</a>'
            
            replacement = f'<a href="{target_filename}" class="tab-link {active_str}">'
            new_html = re.sub(pattern_js, replacement, new_html)
            
            # Actually, to make it idempotent on already processed files:
            # Let's just find the link containing target_tab_id. 
            # Oh wait, the already processed files no longer have target_tab_id in the link!
            # It's better to just use the ORIGINAL files!
            
        for target_tab_id, target_filename in tabs_config.items():
            if target_tab_id == current_tab_id:
                new_html = re.sub(r'<div id="' + target_tab_id + r'" class="' + tab_class + r'" style="display: none;">', f'<div id="{target_tab_id}" class="{tab_class}">', new_html)
            else:
                if f'<div id="{target_tab_id}" class="{tab_class}">' in new_html:
                    new_html = new_html.replace(f'<div id="{target_tab_id}" class="{tab_class}">', f'<div id="{target_tab_id}" class="{tab_class}" style="display: none;">')

        new_html = re.sub(r'function switch[a-zA-Z]+\(tabId, el\) \{.*?\n        \}', '', new_html, flags=re.DOTALL)
        
        with open(f"templates/{current_filename}", 'w', encoding='utf-8') as f:
            f.write(new_html)

vol_tabs = {
    'tab-nearby': 'volunteer-dashboard.html',
    'tab-history': 'volunteer-history.html',
    'tab-certificate': 'volunteer-certificate.html'
}
# We need to run it on the ORIGINAL volunteer-dashboard.html! But I overwrote it!
# Wait, I can restore it from git!
