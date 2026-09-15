import re

new_translations = '''const translations = {
        "Home": "मुख्य पृष्ठ",
        "About": "आमच्याबद्दल",
        "Awareness": "जागरूकता",
        "Accessibility": "सुलभता",
        "Resources": "संसाधने",
        "Assistance": "मदत",
        "Volunteer": "स्वयंसेवक",
        "Report": "अहवाल द्या",
        "Login": "लॉगिन",
        "Dashboard": "डॅशबोर्ड",
        "Logout": "लॉगआउट",
        "Report a Barrier": "अडथळ्याची नोंद करा",
        "Request Help": "मदतीची विनंती",
        "All Requests": "सर्व विनंत्या",
        "My Dashboard": "माझा डॅशबोर्ड",
        "History": "इतिहास",
        "Nearby Requests": "जवळील विनंत्या",
        "Certificate": "प्रमाणपत्र",
        "New Report": "नवीन अहवाल",
        "Physical Barrier Reports": "शारीरिक अडथळे अहवाल",
        "System Settings": "सिस्टीम सेटिंग्ज",
        "Directory": "निर्देशिका",
        "Volunteers": "स्वयंसेवक",
        "Reports": "अहवाल",
        "My History": "माझा इतिहास",
        "Urgent Nearby Requests": "तातडीच्या जवळील विनंत्या",
        "Volunteer Overview": "स्वयंसेवक विहंगावलोकन",
        "Action": "कृती",
        "View": "पहा",
        "Dispatch": "पाठवा",
        "Archive": "संग्रहित करा",
        "Accept Request": "विनंती स्वीकारा",
        "Status": "स्थिती",
        "Location": "स्थान",
        "Severity": "तीव्रता",
        "Issue": "समस्या",
        "Date": "तारीख"
    };'''

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the corrupt translations dictionary
js = re.sub(r'const translations = \{.*?\};', new_translations, js, flags=re.DOTALL)

# Also fix the button text
js = re.sub(r"\? '[^']+' : 'English'", "? 'मराठी' : 'English'", js)
js = re.sub(r"document\.getElementById\('lang-text'\)\.innerText = '[^']+';", "document.getElementById('lang-text').innerText = 'मराठी';", js)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed translations!')
