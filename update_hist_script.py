import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add logic for History tables inside loadDynamicData
history_logic = """
    // User History
    const userHistTbody = document.getElementById('user-history-tbody');
    if (userHistTbody) {
        try {
            const res = await fetch('/api/requests');
            const data = await res.json();
            userHistTbody.innerHTML = '';
            const userEmail = localStorage.getItem('able_email') || 'user@citizen.org';
            const userHistory = data.filter(r => r.email === userEmail && (r.status === 'Resolved' || r.status === 'Completed' || r.status === 'Dispatched'));
            
            if (userHistory.length === 0) {
                userHistTbody.innerHTML = '<tr><td colspan="3" style="text-align:center;">No past requests found.</td></tr>';
            } else {
                userHistory.forEach(req => {
                    const row = `<tr>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">#${req.id}</td>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">${req.req_type}</td>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);"><span style="color: #10b981; font-weight: bold;">${req.status}</span></td>
                    </tr>`;
                    userHistTbody.insertAdjacentHTML('beforeend', row);
                });
            }
        } catch(e) {}
    }

    // Volunteer History
    const volHistTbody = document.getElementById('volunteer-history-tbody');
    if (volHistTbody) {
        try {
            const res = await fetch('/api/requests');
            const data = await res.json();
            volHistTbody.innerHTML = '';
            const volHistory = data.filter(r => r.status === 'Dispatched' || r.status === 'Resolved');
            
            if (volHistory.length === 0) {
                volHistTbody.innerHTML = '<tr><td colspan="3" style="text-align:center;">No past requests fulfilled.</td></tr>';
            } else {
                volHistory.forEach(req => {
                    const row = `<tr>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">#${req.id}</td>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">${req.email}</td>
                        <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">${req.req_type}</td>
                    </tr>`;
                    volHistTbody.insertAdjacentHTML('beforeend', row);
                });
            }
        } catch(e) {}
    }
"""

js = js.replace('    // Admin Pending Volunteers', history_logic + '\n    // Admin Pending Volunteers')

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated script.js to render history tables!")
