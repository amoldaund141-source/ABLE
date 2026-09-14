import re

with open('templates/admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace links
text = re.sub(r'href="javascript:void\(0\);" class="active" onclick="switchAdminTab\(\'(.*?)\', this\)"', r'class="tab-link active" data-tab="\1" style="cursor:pointer;"', text)
text = re.sub(r'href="javascript:void\(0\);" onclick="switchAdminTab\(\'(.*?)\', this\)"', r'class="tab-link" data-tab="\1" style="cursor:pointer;"', text)

# Update script to attach event listeners
script_addition = """
        // Attach click listeners to all tab links
        document.addEventListener("DOMContentLoaded", function() {
            var tabLinks = document.querySelectorAll('.tab-link');
            for (var i = 0; i < tabLinks.length; i++) {
                tabLinks[i].addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = this.getAttribute('data-tab');
                    switchAdminTab(target, this);
                });
            }
        });
"""

# Insert script addition before the switchAdminTab function
text = text.replace('function switchAdminTab(tabId, el) {', script_addition + '\n        function switchAdminTab(tabId, el) {')

with open('templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated admin.html')
