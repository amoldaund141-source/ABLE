import os

with open('templates/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the sidebar
old_sidebar = """                <ul>
                    <li><a href="#" class="active"><span class="material-symbols-outlined">inbox</span> Assistance Requests</a></li>
                    <li><a href="#" onclick="showNotification('Loading Reports...', 'Fetching latest crowdsourced physical barrier reports from the database.', 'report', '#f59e0b'); return false;"><span class="material-symbols-outlined">report</span> Barrier Reports</a></li>
                    <li><a href="#" onclick="showNotification('Volunteer Roster', 'Opening volunteer dispatch and management interface.', 'group', '#3b82f6'); return false;"><span class="material-symbols-outlined">group</span> Manage Volunteers</a></li>
                    <li><a href="#" onclick="showNotification('Updating Directory', 'Opening the verified accessibility directory editor.', 'place', '#10b981'); return false;"><span class="material-symbols-outlined">place</span> Update Directory</a></li>
                    <li><a href="#" onclick="showNotification('System Settings', 'Opening system configuration and access control.', 'settings', '#64748b'); return false;"><span class="material-symbols-outlined">settings</span> Settings</a></li>
                </ul>"""

new_sidebar = """                <ul id="admin-menu">
                    <li><a href="#" class="active" onclick="switchAdminTab(event, 'tab-assistance')"><span class="material-symbols-outlined">inbox</span> Assistance Requests</a></li>
                    <li><a href="#" onclick="switchAdminTab(event, 'tab-reports')"><span class="material-symbols-outlined">report</span> Barrier Reports</a></li>
                    <li><a href="#" onclick="switchAdminTab(event, 'tab-volunteers')"><span class="material-symbols-outlined">group</span> Manage Volunteers</a></li>
                    <li><a href="#" onclick="switchAdminTab(event, 'tab-directory')"><span class="material-symbols-outlined">place</span> Update Directory</a></li>
                    <li><a href="#" onclick="switchAdminTab(event, 'tab-settings')"><span class="material-symbols-outlined">settings</span> Settings</a></li>
                </ul>"""

content = content.replace(old_sidebar, new_sidebar)

# 2. Wrap existing section content in tab-assistance
content = content.replace('<section>', '<section id="main-content">\n                <div id="tab-assistance" class="admin-tab">')
# Close tab-assistance right before </section>
content = content.replace('            </section>', '                </div>\n            </section>')

# 3. Add other tabs
other_tabs = """
                <!-- Barrier Reports Tab -->
                <div id="tab-reports" class="admin-tab" style="display: none;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                        <h2>Physical Barrier Reports</h2>
                        <button class="btn" onclick="showNotification('New Report', 'Opening barrier submission form...', 'add', '#2563eb')"><span class="material-symbols-outlined" style="margin-right: 8px;">add</span> New Report</button>
                    </div>
                    <div class="card" style="padding: 0; overflow-x: auto;">
                        <table class="request-table">
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>Location</th>
                                    <th>Issue</th>
                                    <th>Severity</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Today</td>
                                    <td>Deccan Gymkhana</td>
                                    <td>Broken Wheelchair Ramp</td>
                                    <td><span style="color: #ef4444; font-weight: bold;">High</span></td>
                                    <td><span class="status-badge status-pending">Investigating</span></td>
                                </tr>
                                <tr>
                                    <td>Yesterday</td>
                                    <td>Shivaji Nagar Station</td>
                                    <td>Elevator Out of Order</td>
                                    <td><span style="color: #ef4444; font-weight: bold;">High</span></td>
                                    <td><span class="status-badge status-active">Repair Dispatched</span></td>
                                </tr>
                                <tr>
                                    <td>3 days ago</td>
                                    <td>FC Road</td>
                                    <td>Obstructed Tactile Path</td>
                                    <td><span style="color: #f59e0b; font-weight: bold;">Medium</span></td>
                                    <td><span class="status-badge status-resolved">Resolved</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Volunteers Tab -->
                <div id="tab-volunteers" class="admin-tab" style="display: none;">
                    <h2>Manage Volunteers</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Review and approve NSS volunteer applications.</p>
                    <div class="card" style="padding: 40px; text-align: center;">
                        <span class="material-symbols-outlined" style="font-size: 4rem; color: var(--brand-blue); margin-bottom: 10px;">verified_user</span>
                        <h3 style="margin-bottom: 10px;">All Volunteers Active</h3>
                        <p style="color: var(--text-muted);">There are no pending applications requiring your approval at this time.</p>
                    </div>
                </div>

                <!-- Directory Tab -->
                <div id="tab-directory" class="admin-tab" style="display: none;">
                    <h2>Update Accessibility Directory</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Add verified accessible locations to the database.</p>
                    <div class="card" style="padding: 30px; max-width: 500px;">
                        <form onsubmit="event.preventDefault(); showNotification('Success!', 'Directory updated securely.', 'check_circle', '#10b981'); this.reset();">
                            <div style="margin-bottom: 15px;">
                                <label style="display: block; margin-bottom: 5px;">Location Name</label>
                                <input type="text" placeholder="E.g. Pune Central Mall" required style="width: 100%;">
                            </div>
                            <div style="margin-bottom: 20px;">
                                <label style="display: block; margin-bottom: 5px;">Primary Feature</label>
                                <select style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid var(--border-light); background: var(--bg-surface); color: var(--text-main);">
                                    <option>Wheelchair Ramp</option>
                                    <option>Elevator</option>
                                    <option>Tactile Paths</option>
                                </select>
                            </div>
                            <button type="submit" class="btn">Add Location</button>
                        </form>
                    </div>
                </div>

                <!-- Settings Tab -->
                <div id="tab-settings" class="admin-tab" style="display: none;">
                    <h2>System Settings</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Configure backend API integrations and system behavior.</p>
                    <div class="card" style="padding: 30px;">
                        <h4 style="margin-bottom: 15px; border-bottom: 1px solid var(--border-light); padding-bottom: 10px;">API Integrations</h4>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                            <span>Twilio SMS Gateway</span>
                            <span style="color: #10b981; font-weight: bold;">Connected</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                            <span>OpenStreetMap Sync</span>
                            <span style="color: #10b981; font-weight: bold;">Connected</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>PostgreSQL Database</span>
                            <span style="color: #10b981; font-weight: bold;">Healthy</span>
                        </div>
                    </div>
                </div>
"""

content = content.replace('                </div>\n            </section>', '                </div>\n' + other_tabs + '\n            </section>')

# 4. Add the JS function
js = """
    <script>
        function switchAdminTab(event, tabId) {
            // Update active class on menu
            document.querySelectorAll('#admin-menu a').forEach(a => a.classList.remove('active'));
            event.currentTarget.classList.add('active');

            // Hide all tabs
            document.querySelectorAll('.admin-tab').forEach(tab => {
                tab.style.display = 'none';
            });

            // Show selected tab
            document.getElementById(tabId).style.display = 'block';
        }
    </script>
"""

content = content.replace('</body>', js + '\n</body>')

with open('templates/admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Admin tabs added.")
