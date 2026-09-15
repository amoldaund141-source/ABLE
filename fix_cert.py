import re

new_cert = '''<div class="card" style="padding: 50px 30px; text-align: center; border: 2px dashed #f59e0b; background: linear-gradient(145deg, var(--bg-surface) 0%, rgba(245,158,11,0.05) 100%); align-items: center;">
                        <span class="material-symbols-outlined" style="font-size: 6rem; color: #f59e0b; margin-bottom: 20px; filter: drop-shadow(0 4px 6px rgba(245,158,11,0.2));">workspace_premium</span>
                        <h3 style="margin-bottom: 15px; font-size: 2rem; font-family: 'Georgia', serif; color: #f59e0b;">Certificate of Appreciation</h3>
                        <p style="color: var(--text-main); font-size: 1.1rem; margin-bottom: 40px; line-height: 1.6; max-width: 500px;">This certificate is proudly presented to<br><strong style="font-size: 1.6rem; display: block; margin: 15px 0; color: var(--text-main);">NSS Volunteer</strong>for completing 10+ hours of dedicated accessibility assistance.</p>
                        <button class="btn" style="align-self: center; background: #f59e0b; color: white; border: none; padding: 12px 30px; font-size: 1.1rem; box-shadow: 0 4px 14px rgba(245,158,11,0.4); border-radius: 50px;" onclick="showNotification('Downloading', 'Your PDF certificate is being generated...', 'download', '#10b981')"><span class="material-symbols-outlined" style="margin-right: 8px; vertical-align: middle;">download</span> Download Official PDF</button>
                    </div>'''

with open('templates/volunteer-certificate.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the old certificate div
old_cert_regex = r'<div class="card" style="padding: 40px; text-align: center; border: 2px dashed var\(--brand-blue\);">.*?</div>'
html = re.sub(old_cert_regex, new_cert, html, flags=re.DOTALL)

with open('templates/volunteer-certificate.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated certificate layout!')
