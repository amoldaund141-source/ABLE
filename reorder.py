import os

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Stats Section
stats_start = content.find('<!-- Stats Section -->')
stats_end = content.find('</section>', stats_start) + len('</section>')
stats_html = content[stats_start:stats_end]

# Remove Stats Section
content = content[:stats_start] + content[stats_end:]

# Insert Stats Section before Partners Section
partners_start = content.find('<!-- Partners Section -->')
content = content[:partners_start] + stats_html + '\n\n        ' + content[partners_start:]

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Order updated successfully.")
