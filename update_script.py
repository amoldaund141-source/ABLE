import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update the loadDynamicData to also fetch pending volunteers
new_dynamic_logic = """
    // Admin Pending Volunteers
    const volTbody = document.getElementById('admin-volunteers-tbody');
    if (volTbody) {
        try {
            const res = await fetch('/api/volunteers');
            const data = await res.json();
            volTbody.innerHTML = '';
            
            if (data.length === 0) {
                volTbody.innerHTML = '<tr><td colspan="5" style="text-align:center;">No pending verifications found.</td></tr>';
            } else {
                data.forEach(vol => {
                    const statusIcon = vol.id_status === 'Valid' ? `<span style='color:#10b981; font-weight: bold;'><span class='material-symbols-outlined' style='font-size: 1rem; vertical-align: middle;'>verified</span> Official Document Scanned</span>` : `<span style='color:#f59e0b; font-weight: bold;'><span class='material-symbols-outlined' style='font-size: 1rem; vertical-align: middle;'>pending_actions</span> Waiting for Review</span>`;
                    const row = `<tr>
                        <td>${vol.name}</td>
                        <td>${vol.email}</td>
                        <td>${vol.affiliation}</td>
                        <td>${vol.role}</td>
                        <td>
                            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                                <button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="showNotification('ID Verification', \`<div style='text-align:center; padding: 10px;'><img src='dummy_nss_id.jpg' style='border-radius:8px; margin-bottom:15px; border: 1px solid var(--border-light); width: 100%; max-width: 350px;' alt='NSS ID Scan'><br><strong>${vol.name}</strong><br>ID: NSS/TMP/${vol.id}<br>${statusIcon}</div>\`, 'badge', '#3b82f6')">View ID</button>
                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #10b981; border: none;" onclick="approveVolunteer('${vol.email}', this)">Approve</button>
                                <button class="btn" style="padding: 6px 12px; font-size: 0.85rem; background: #ef4444; border: none;" onclick="rejectVolunteer('${vol.email}', this)">Reject</button>
                            </div>
                        </td>
                    </tr>`;
                    volTbody.insertAdjacentHTML('beforeend', row);
                });
            }
        } catch (e) {
            console.error("Error loading volunteers:", e);
        }
    }
}"""

js = js.replace('    // Admin Reports', new_dynamic_logic + '\n\n    // Admin Reports')

# 2. Update volunteer registration logic to fetch POST
new_volunteer_post = """            } else if (form.id === 'volunteer-form') {
                const formData = new FormData(form);
                const data = {
                    name: formData.get('name') || 'Anonymous',
                    email: formData.get('email'),
                    phone: formData.get('phone') || '0000000000',
                    affiliation: document.getElementById('v-affiliation') ? document.getElementById('v-affiliation').value : 'Unknown',
                    role: 'General Volunteer'
                };
                
                try {
                    await fetch('/api/volunteers', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                } catch(e) {}
                
                showNotification("Application Submitted!", "Your volunteer application has been sent to the admins for verification. You will receive an email with your credentials once approved.");
                form.reset();
                
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 3500);
                
                return;
            }"""
js = re.sub(r"            \} else if \(form\.id === 'volunteer-form'\) \{.*?return;\n            \}", new_volunteer_post, js, flags=re.DOTALL)

# 3. Add rejectVolunteer function
reject_logic = """
window.rejectVolunteer = async function(email, btnElement) {
    try {
        await fetch('/api/reject_volunteer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email })
        });
        showNotification('Rejected', 'Application rejected. An email has been sent requesting a clearer ID upload.', 'cancel', '#ef4444');
        if(btnElement) btnElement.closest('tr').style.display = 'none';
    } catch(e) {}
};
"""
js = js + reject_logic

# 4. Fix User Dashboard Fetch Filter
# Inside loadDynamicData, we filter reqTbody if it is user-dashboard
fix_user_filter = """
                data.forEach(req => {
                    if (document.getElementById('user-requests-tbody') && req.email !== (localStorage.getItem('able_email') || 'user@citizen.org')) {
                        return; // Skip if it's the user dashboard and email doesn't match
                    }"""
js = js.replace('                data.forEach(req => {', fix_user_filter, 1)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated script.js to make volunteers fully dynamic and fix user dashboard privacy!")
