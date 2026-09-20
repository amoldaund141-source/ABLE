import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_volunteer_logic = """            } else if (form.id === 'volunteer-form') {
                const formData = new FormData(form);
                const email = formData.get('email');
                
                localStorage.setItem('able_logged_in', 'true');
                localStorage.setItem('able_role', 'volunteer');
                if (email) localStorage.setItem('able_email', email);
                
                showNotification("Success!", "Registration complete! Welcome to the team. Redirecting to your dashboard...");
                
                setTimeout(() => {
                    window.location.href = 'volunteer-dashboard.html';
                }, 2000);
                
                return;
            }"""

js = re.sub(r"            \} else if \(form\.id === 'volunteer-form'\) \{.*?return;\n            \}", new_volunteer_logic, js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated volunteer registration logic!")
