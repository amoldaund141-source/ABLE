import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the Emergency SOS Button HTML
text = re.sub(r'\s*<!-- Emergency SOS Button -->.*?</span>\s*</div>', '', text, flags=re.DOTALL)

# 2. Remove the SOS Cancel Modal HTML
text = re.sub(r'\s*<!-- SOS Cancel Modal -->.*?</div>\n', '\n', text, flags=re.DOTALL)

# 3. Remove the SOS Logic block and cancelSOS function
# We stop exactly at "// Text-to-Speech Logic"
text = re.sub(r'\s*// SOS Logic.*?(?=\s*// Text-to-Speech Logic)', '\n\n', text, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SOS removed perfectly.")
