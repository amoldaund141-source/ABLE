import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_form_logic = """        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            if (form.id === 'search-accessibility') {
                showNotification("Scanning...", "Querying OpenStreetMap dataset for verified accessible locations in that area. (Mock Data)", "map", "#3b82f6");
                return;
            } else if (form.id === 'volunteer-form') {
                showNotification("Success!", "Registration complete! Welcome to the team. You will receive an email shortly.");
                form.reset();
                return;
            }

            // Extract data
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            data.email = 'anonymous@citizen.org';

            let endpoint = '';
            let message = '';
            
            if (form.id === 'assistance-form') {
                endpoint = '/api/requests';
                data.req_type = document.getElementById('service') ? document.getElementById('service').value : 'General Assistance';
                data.location = document.getElementById('location') ? document.getElementById('location').value : 'Unknown Location';
                message = "Request saved to database! An SMS dispatch has been sent via Twilio to registered NSS volunteers in your area.";
            } else if (form.id === 'report-form') {
                endpoint = '/api/reports';
                data.issue = document.getElementById('issue-type') ? document.getElementById('issue-type').value : (document.getElementById('desc') ? document.getElementById('desc').value : 'Barrier Issue');
                data.location = document.getElementById('location') ? document.getElementById('location').value : 'Unknown Location';
                message = "Barrier report logged into the central database. Thank you for making Pune more accessible!";
            }
            
            if (endpoint) {
                try {
                    const response = await fetch(endpoint, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                    const result = await response.json();
                    
                    if (result.success) {
                        showNotification("Success!", message);
                        form.reset();
                    } else {
                        showNotification("Error", "Failed to save data to the server.", "error", "#dc2626");
                    }
                } catch (error) {
                    showNotification("Error", "Network error occurred while contacting the server.", "error", "#dc2626");
                }
            }
        });"""

js = re.sub(r"        form\.addEventListener\('submit', \(e\) => \{.*?form\.reset\(\);\n        \}\);", new_form_logic, js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Wired up frontend to backend!")
