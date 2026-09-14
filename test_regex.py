import re
text = 'href="#" class="tab-link active" onclick="switchAdminTab(event, \'tab-dashboard\', this)"'
match = re.search(r'href="#" class="tab-link (active )?" onclick="switchAdminTab\(event, \'(.*?)\', this\)"', text)
print(bool(match))
