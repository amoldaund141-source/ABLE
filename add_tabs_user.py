import os

# --- USER DASHBOARD ---
with open('templates/user-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_sidebar = """                <ul>
                    <li><a href="#" class="active"><span class="material-symbols-outlined">pending_actions</span> Active Requests</a></li>
                    <li><a href="#" onclick="showNotification('Loading History', 'Fetching your past requests from the database...', 'history', '#3b82f6'); return false;"><span class="material-symbols-outlined">history</span> Past Requests</a></li>
                </ul>"""

new_sidebar = """                <ul id="user-menu">
                    <li><a href="#" class="active" onclick="switchUserTab(event, 'tab-active')"><span class="material-symbols-outlined">pending_actions</span> Active Requests</a></li>
                    <li><a href="#" onclick="switchUserTab(event, 'tab-history')"><span class="material-symbols-outlined">history</span> Past Requests</a></li>
                </ul>"""
content = content.replace(old_sidebar, new_sidebar)

content = content.replace('<section>', '<section id="main-content">\n                <div id="tab-active" class="user-tab">')
content = content.replace('            </section>', '                </div>\n            </section>')

other_tabs = """
                <!-- History Tab -->
                <div id="tab-history" class="user-tab" style="display: none;">
                    <h2>Past Requests History</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">View your previous assistance requests and reports.</p>
                    <div class="card" style="padding: 0; overflow-x: auto;">
                        <table class="request-table" style="width: 100%; border-collapse: collapse;">
                            <thead>
                                <tr>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Date</th>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Type</th>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">August 12, 2026</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">Visual Assistance</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);"><span style="color: #10b981; font-weight: bold;">Completed</span></td>
                                </tr>
                                <tr>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">July 4, 2026</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">Mobility Escort</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);"><span style="color: #10b981; font-weight: bold;">Completed</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
"""
content = content.replace('                </div>\n            </section>', '                </div>\n' + other_tabs + '\n            </section>')

js = """
    <script>
        function switchUserTab(event, tabId) {
            document.querySelectorAll('#user-menu a').forEach(a => a.classList.remove('active'));
            event.currentTarget.classList.add('active');
            document.querySelectorAll('.user-tab').forEach(tab => tab.style.display = 'none');
            document.getElementById(tabId).style.display = 'block';
        }
    </script>
"""
content = content.replace('</body>', js + '\n</body>')
with open('templates/user-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)


# --- VOLUNTEER DASHBOARD ---
with open('templates/volunteer-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_sidebar = """                <ul>
                    <li><a href="#" class="active"><span class="material-symbols-outlined">map</span> Nearby Requests</a></li>
                    <li><a href="#" onclick="showNotification('Loading History', 'Fetching your volunteer history from the database...', 'history', '#3b82f6'); return false;"><span class="material-symbols-outlined">history</span> My History</a></li>
                    <li><a href="#" onclick="showNotification('Generating Certificate', 'Compiling your volunteer hours and generating a signed PDF certificate...', 'workspace_premium', '#f59e0b'); return false;"><span class="material-symbols-outlined">workspace_premium</span> Certificate</a></li>
                </ul>"""

new_sidebar = """                <ul id="vol-menu">
                    <li><a href="#" class="active" onclick="switchVolTab(event, 'tab-nearby')"><span class="material-symbols-outlined">map</span> Nearby Requests</a></li>
                    <li><a href="#" onclick="switchVolTab(event, 'tab-history')"><span class="material-symbols-outlined">history</span> My History</a></li>
                    <li><a href="#" onclick="switchVolTab(event, 'tab-certificate')"><span class="material-symbols-outlined">workspace_premium</span> Certificate</a></li>
                </ul>"""
content = content.replace(old_sidebar, new_sidebar)

content = content.replace('<section>', '<section id="main-content">\n                <div id="tab-nearby" class="vol-tab">')
content = content.replace('            </section>', '                </div>\n            </section>')

other_tabs = """
                <!-- History Tab -->
                <div id="tab-history" class="vol-tab" style="display: none;">
                    <h2>Volunteer History</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Review the citizens you have helped.</p>
                    <div class="card" style="padding: 0; overflow-x: auto;">
                        <table class="request-table" style="width: 100%; border-collapse: collapse;">
                            <thead>
                                <tr>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Date</th>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Citizen</th>
                                    <th style="padding: 16px; border-bottom: 1px solid var(--border-light); text-align: left;">Assistance Type</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">Yesterday</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">Priya K.</td>
                                    <td style="padding: 16px; border-bottom: 1px solid var(--border-light);">Campus Navigation</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Certificate Tab -->
                <div id="tab-certificate" class="vol-tab" style="display: none;">
                    <h2>NSS Volunteer Certificate</h2>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Download your official digitally signed certificate.</p>
                    <div class="card" style="padding: 40px; text-align: center; border: 2px dashed var(--brand-blue);">
                        <span class="material-symbols-outlined" style="font-size: 5rem; color: #f59e0b; margin-bottom: 20px;">workspace_premium</span>
                        <h3 style="margin-bottom: 10px;">Certificate of Appreciation</h3>
                        <p style="color: var(--text-muted); margin-bottom: 30px;">Awarded for completing 10+ hours of accessibility assistance.</p>
                        <button class="btn" onclick="showNotification('Downloading', 'Your PDF certificate is being generated...', 'download', '#10b981')"><span class="material-symbols-outlined" style="margin-right: 8px;">download</span> Download PDF</button>
                    </div>
                </div>
"""
content = content.replace('                </div>\n            </section>', '                </div>\n' + other_tabs + '\n            </section>')

js = """
    <script>
        function switchVolTab(event, tabId) {
            document.querySelectorAll('#vol-menu a').forEach(a => a.classList.remove('active'));
            event.currentTarget.classList.add('active');
            document.querySelectorAll('.vol-tab').forEach(tab => tab.style.display = 'none');
            document.getElementById(tabId).style.display = 'block';
        }
    </script>
"""
content = content.replace('</body>', js + '\n</body>')
with open('templates/volunteer-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("User and Vol tabs added.")
