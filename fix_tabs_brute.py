import re

for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    func = "switchAdminTab" if "admin" in filename else "switchUserTab" if "user" in filename else "switchVolTab"

    # Brute force replace
    text = text.replace('class="tab-link active" data-tab="tab-dashboard" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-dashboard\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-dashboard" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-dashboard\', this)"')

    text = text.replace('class="tab-link active" data-tab="tab-requests" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-requests\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-requests" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-requests\', this)"')

    text = text.replace('class="tab-link active" data-tab="tab-reports" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-reports\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-reports" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-reports\', this)"')

    text = text.replace('class="tab-link active" data-tab="tab-volunteers" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-volunteers\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-volunteers" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-volunteers\', this)"')

    text = text.replace('class="tab-link active" data-tab="tab-directory" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-directory\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-directory" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-directory\', this)"')

    text = text.replace('class="tab-link active" data-tab="tab-settings" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-settings\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-settings" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-settings\', this)"')

    # user tabs
    text = text.replace('class="tab-link active" data-tab="tab-active" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-active\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-active" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-active\', this)"')
    text = text.replace('class="tab-link active" data-tab="tab-history" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-history\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-history" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-history\', this)"')

    # vol tabs
    text = text.replace('class="tab-link active" data-tab="tab-nearby" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-nearby\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-nearby" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-nearby\', this)"')
    text = text.replace('class="tab-link active" data-tab="tab-certificate" style="cursor:pointer;"', f'href="#" class="tab-link active" onclick="{func}(event, \'tab-certificate\', this)"')
    text = text.replace('class="tab-link" data-tab="tab-certificate" style="cursor:pointer;"', f'href="#" class="tab-link" onclick="{func}(event, \'tab-certificate\', this)"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Brute force replaced.")
