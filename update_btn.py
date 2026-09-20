import glob
import re

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    old_btn = """<button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to sneha.s@student.org', 'mail', '#10b981'); this.parentElement.parentElement.parentElement.style.display='none';">Approve</button>"""
    new_btn = """<button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="approveVolunteer('sneha.s@student.org', this)">Approve</button>"""
    
    html = html.replace(old_btn, new_btn)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated Approve button to use backend API!")
