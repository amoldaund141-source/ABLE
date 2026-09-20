import glob
import re

# 1. Update volunteer.html to add the ID upload field
with open('templates/volunteer.html', 'r', encoding='utf-8') as f:
    html = f.read()

id_upload_field = """                    </div>

                    <div style="margin-bottom: 20px;">
                        <label for="v-id-upload">ID Verification Document (Required)</label>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px;">Upload your NSS ID, College ID, or Aadhaar Card for admin verification.</p>
                        <input type="file" id="v-id-upload" name="v-id-upload" accept="image/png, image/jpeg, application/pdf" required style="background: var(--bg-page); padding: 8px; cursor: pointer;">"""

html = re.sub(r'                    </div>\s*<div style="margin-bottom: 20px;">\s*<label>How would you like to contribute\?</label>', id_upload_field + '\n                    </div>\n\n                    <div style="margin-bottom: 20px;">\n                        <label>How would you like to contribute?</label>', html)

with open('templates/volunteer.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update all admin*.html files to include the View ID button
files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    old_td = """                                        <td>
                                            <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to rahul.d@student.org', 'mail', '#10b981'); this.parentElement.parentElement.style.display='none';">Approve & Send Credentials</button>
                                        </td>"""
    
    new_td = """                                        <td>
                                            <div style="display: flex; gap: 8px;">
                                                <button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="showNotification('ID Verification', `<div style='text-align:center; padding: 10px;'><img src='https://images.unsplash.com/photo-1593012891334-0131495c553f?auto=format&fit=crop&q=80&w=200&h=120' style='border-radius:8px; margin-bottom:15px; border: 1px solid var(--border-light);'><br><strong>Rahul Deshmukh</strong><br>ID: NSS-2023-8472<br><span style='color:#10b981; font-weight: bold;'><span class='material-symbols-outlined' style='font-size: 1rem; vertical-align: middle;'>verified</span> Document Scanned & Valid</span></div>`, 'badge', '#3b82f6')">View ID</button>
                                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to rahul.d@student.org', 'mail', '#10b981'); this.parentElement.parentElement.parentElement.style.display='none';">Approve</button>
                                            </div>
                                        </td>"""
    
    html = html.replace(old_td, new_td)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Added document upload and admin verification UI!")
