import glob
import re

# 1. Update script.js to change the volunteer registration workflow to "Pending Approval"
with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_volunteer_logic = """            } else if (form.id === 'volunteer-form') {
                const formData = new FormData(form);
                const email = formData.get('email') || 'volunteer@nss.org';
                
                showNotification("Application Submitted!", "Your volunteer application has been sent to the admins for verification. You will receive an email with your credentials once approved.");
                form.reset();
                
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 3500);
                
                return;
            }"""

js = re.sub(r"            \} else if \(form\.id === 'volunteer-form'\) \{.*?return;\n            \}", new_volunteer_logic, js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Update the admin-volunteers HTML tab to show a pending applications table
new_tab_volunteers = """                <div id="tab-volunteers" class="admin-tab"{display_style}>
                    <h2>Manage Volunteers</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Review and approve NSS volunteer applications.</p>
                    
                    <div class="card" style="margin-bottom: 30px;">
                        <h3 style="margin-bottom: 15px;">Pending Verifications</h3>
                        <div class="table-responsive">
                            <table class="request-table">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Email</th>
                                        <th>Affiliation</th>
                                        <th>Contribution Role</th>
                                        <th>Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Rahul Deshmukh</td>
                                        <td>rahul.d@student.org</td>
                                        <td>NSS Student</td>
                                        <td>On-ground physical assistance</td>
                                        <td>
                                            <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981;" onclick="showNotification('Approved', 'Volunteer verified! Credentials have been automatically emailed to rahul.d@student.org', 'mail', '#10b981'); this.parentElement.parentElement.style.display='none';">Approve & Send Credentials</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <div class="card" style="padding: 40px; text-align: center;">
                        <span class="material-symbols-outlined" style="font-size: 4rem; color: var(--brand-blue); margin-bottom: 10px;">verified_user</span>
                        <h3 style="margin-bottom: 10px;">42 Active Volunteers</h3>
                        <p style="color: var(--text-muted);">All approved volunteers are actively monitored in the central database.</p>
                    </div>
                </div>"""

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    display_style = '' if 'admin-volunteers.html' in file else ' style="display: none;"'
    current_replacement = new_tab_volunteers.format(display_style=display_style)
    
    html = re.sub(r'<div id="tab-volunteers" class="admin-tab".*?</div>\s*</div>', current_replacement, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Added volunteer verification workflow!")
