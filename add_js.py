with open('static/script.js', 'a', encoding='utf-8') as f:
    f.write('''

// --- Admin Actions ---
window.approveVolunteer = async function(email, btnElement) {
    try {
        const response = await fetch('/api/approve_volunteer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: 'vol123' })
        });
        const result = await response.json();
        
        if (result.success) {
            showNotification('Approved & Account Created', `Volunteer verified! The account for ${email} has been created in the database. An automated email with the password 'vol123' has been sent.`, 'mail', '#10b981');
            // Hide the row
            if(btnElement) {
                btnElement.closest('tr').style.display = 'none';
            }
        } else {
            showNotification('Error', 'Could not create account in database.', 'error', '#dc2626');
        }
    } catch (error) {
        showNotification('Error', 'Network error connecting to backend.', 'error', '#dc2626');
    }
};
''')
print("Added approveVolunteer function to script.js!")
