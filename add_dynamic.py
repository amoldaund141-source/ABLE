with open('static/script.js', 'a', encoding='utf-8') as f:
    f.write('''

// --- Dynamic Data Fetching ---
async function loadDynamicData() {
    // Admin & User Requests
    const reqTbody = document.getElementById('admin-requests-tbody') || document.getElementById('user-requests-tbody');
    if (reqTbody) {
        try {
            const res = await fetch('/api/requests');
            const data = await res.json();
            reqTbody.innerHTML = '';
            
            if (data.length === 0) {
                reqTbody.innerHTML = '<tr><td colspan="6" style="text-align:center;">No requests found.</td></tr>';
            } else {
                data.forEach(req => {
                    const statusClass = req.status === 'Pending' ? 'status-pending' : (req.status === 'Dispatched' ? 'status-active' : 'status-resolved');
                    
                    let actionBtn = '';
                    if (req.status === 'Pending' && document.getElementById('admin-requests-tbody')) {
                        actionBtn = `<button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="dispatchRequest(${req.id}, this)">Dispatch</button>`;
                    } else if (req.status === 'Dispatched') {
                        actionBtn = `<span style="color: var(--text-muted); font-size: 0.85rem;">Assigned</span>`;
                    }
                    
                    const row = `<tr>
                        <td>#${req.id}</td>
                        <td>${req.email}</td>
                        <td>${req.location}</td>
                        <td>${req.req_type}</td>
                        <td><span class="status-badge ${statusClass}">${req.status}</span></td>
                        <td>${actionBtn}</td>
                    </tr>`;
                    reqTbody.insertAdjacentHTML('beforeend', row);
                });
            }
        } catch (e) {
            console.error("Error loading requests:", e);
        }
    }

    // Admin Reports
    const repTbody = document.getElementById('admin-reports-tbody');
    if (repTbody) {
        try {
            const res = await fetch('/api/reports');
            const data = await res.json();
            repTbody.innerHTML = '';
            
            if (data.length === 0) {
                repTbody.innerHTML = '<tr><td colspan="6" style="text-align:center;">No barrier reports found.</td></tr>';
            } else {
                data.forEach(rep => {
                    const sevColor = rep.severity === 'High' ? '#ef4444' : (rep.severity === 'Medium' ? '#f59e0b' : '#3b82f6');
                    const row = `<tr>
                        <td>${rep.date || 'Today'}</td>
                        <td>${rep.location}</td>
                        <td>${rep.issue}</td>
                        <td><span style="color: ${sevColor}; font-weight: bold;">${rep.severity}</span></td>
                        <td><span class="status-badge status-pending">${rep.status}</span></td>
                        <td>
                            <button class="btn secondary" style="padding: 6px 12px; font-size: 0.85rem;" onclick="showNotification('Report #${rep.id}', \`<div style='text-align:left; padding:10px;'><p><strong>Reporter:</strong> ${rep.email}</p><p><strong>Location:</strong> ${rep.location}</p><p><strong>Issue:</strong> ${rep.issue}</p></div>\`, 'visibility', '#3b82f6')">View</button>
                        </td>
                    </tr>`;
                    repTbody.insertAdjacentHTML('beforeend', row);
                });
            }
        } catch (e) {
            console.error("Error loading reports:", e);
        }
    }
}

window.dispatchRequest = async function(id, btn) {
    try {
        const res = await fetch(`/api/requests/${id}/accept`, { method: 'POST' });
        const result = await res.json();
        if (result.success) {
            showNotification('Dispatched', 'Request has been dispatched to the nearest volunteer!', 'send', '#10b981');
            btn.parentElement.previousElementSibling.innerHTML = '<span class="status-badge status-active">Dispatched</span>';
            btn.outerHTML = '<span style="color: var(--text-muted); font-size: 0.85rem;">Assigned</span>';
        }
    } catch (e) {
        console.error(e);
    }
};

// Call on load
document.addEventListener('DOMContentLoaded', () => {
    loadDynamicData();
});
''')
print("Added dynamic table rendering to script.js!")
