import glob

old_html = """                                        <td>
                                            <div style="display: flex; gap: 8px;">
                                                <button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="showNotification('ID Verification', `<div style='text-align:center; padding: 10px;'><img src='https://images.unsplash.com/photo-1593012891334-0131495c553f?auto=format&fit=crop&q=80&w=200&h=120' style='border-radius:8px; margin-bottom:15px; border: 1px solid var(--border-light);'><br><strong>Rahul Deshmukh</strong><br>ID: NSS-2023-8472<br><span style='color:#10b981; font-weight: bold;'><span class='material-symbols-outlined' style='font-size: 1rem; vertical-align: middle;'>verified</span> Document Scanned & Valid</span></div>`, 'badge', '#3b82f6')">View ID</button>
                                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to rahul.d@student.org', 'mail', '#10b981'); this.parentElement.parentElement.parentElement.style.display='none';">Approve</button>
                                            </div>
                                        </td>"""

new_html = """                                        <td>
                                            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                                                <button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="showNotification('ID Verification', `<div style='text-align:center; padding: 10px;'><img src='https://dummyimage.com/300x180/334155/f8fafc.png&text=Uploaded+ID+Card+Scan' style='border-radius:8px; margin-bottom:15px; border: 1px solid var(--border-light); width: 100%; max-width: 300px;' alt='ID Scan'><br><strong>Rahul Deshmukh</strong><br>ID: NSS-2023-8472<br><span style='color:#10b981; font-weight: bold;'><span class='material-symbols-outlined' style='font-size: 1rem; vertical-align: middle;'>verified</span> System Pre-Check Passed</span></div>`, 'badge', '#3b82f6')">View ID</button>
                                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to rahul.d@student.org', 'mail', '#10b981'); this.parentElement.parentElement.parentElement.style.display='none';">Approve</button>
                                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #ef4444; border: none;" onclick="showNotification('Rejected', 'Application rejected. An email has been sent requesting a clearer ID upload.', 'cancel', '#ef4444'); this.parentElement.parentElement.parentElement.style.display='none';">Reject</button>
                                            </div>
                                        </td>"""

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(old_html, new_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed broken image and added Reject button!")
