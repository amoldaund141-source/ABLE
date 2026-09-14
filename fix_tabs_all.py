import re

for filename, func_name in [('templates/user-dashboard.html', 'switchUserTab'), ('templates/volunteer-dashboard.html', 'switchVolTab')]:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace links
    text = re.sub(r'href="javascript:void\(0\);" class="active" onclick="' + func_name + r'\(\'(.*?)\', this\)"', r'class="tab-link active" data-tab="\1" style="cursor:pointer;"', text)
    text = re.sub(r'href="javascript:void\(0\);" onclick="' + func_name + r'\(\'(.*?)\', this\)"', r'class="tab-link" data-tab="\1" style="cursor:pointer;"', text)

    # Update script to attach event listeners
    script_addition = """
        // Attach click listeners to all tab links
        document.addEventListener("DOMContentLoaded", function() {
            var tabLinks = document.querySelectorAll('.tab-link');
            for (var i = 0; i < tabLinks.length; i++) {
                tabLinks[i].addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = this.getAttribute('data-tab');
                    """ + func_name + """(target, this);
                });
            }
        });
    """

    # Insert script addition before the switch function
    text = text.replace(f'function {func_name}(tabId, el) {{', script_addition + f'\n        function {func_name}(tabId, el) {{')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print('Updated user and volunteer dashboards')
