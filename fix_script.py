import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

admin_nav = """
                <li><a href="index.html">Home</a></li>
                <li><a href="admin.html"><span class="material-symbols-outlined" style="vertical-align: middle;">space_dashboard</span> Dashboard</a></li>
                <li><a href="admin-requests.html"><span class="material-symbols-outlined" style="vertical-align: middle;">inbox</span> All Requests</a></li>
                <li><a href="admin-volunteers.html"><span class="material-symbols-outlined" style="vertical-align: middle;">group</span> Volunteers</a></li>
                <li><a href="admin-reports.html"><span class="material-symbols-outlined" style="vertical-align: middle;">analytics</span> Reports</a></li>
                <li><a href="admin-directory.html"><span class="material-symbols-outlined" style="vertical-align: middle;">place</span> Directory</a></li>
                <li><a href="admin-settings.html"><span class="material-symbols-outlined" style="vertical-align: middle;">settings</span> Settings</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
"""

volunteer_nav = """
                <li><a href="index.html">Home</a></li>
                <li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> My Dashboard</a></li>
                <li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Nearby Requests</a></li>
                <li><a href="volunteer-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> My History</a></li>
                <li><a href="volunteer-certificate.html"><span class="material-symbols-outlined" style="vertical-align: middle;">workspace_premium</span> Certificate</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
"""

user_nav = """
                <li><a href="index.html">Home</a></li>
                <li><a href="user-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> Active Requests</a></li>
                <li><a href="user-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> Past Requests</a></li>
                <li><a href="assistance.html"><span class="material-symbols-outlined" style="vertical-align: middle;">health_and_safety</span> New Request</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
"""

js = re.sub(r'(if \(userRole === \'admin\'\) \{\s*navUl\.innerHTML = `).*?(`;\s*\} else if \(userRole === \'volunteer\'\) \{\s*navUl\.innerHTML = `).*?(`;\s*\} else \{\s*// Standard Citizen.*?navUl\.innerHTML = `).*?(`;\s*\})', r'\g<1>' + admin_nav + r'\g<2>' + volunteer_nav + r'\g<3>' + user_nav + r'\g<4>', js, flags=re.DOTALL)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed script.js')
