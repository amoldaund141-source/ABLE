import re

with open('templates/resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update onclick handlers
content = content.replace(
    "onclick=\"showNotification('Opening National Government Scheme Portal in a new tab...', 'success'); return false;\"",
    "onclick=\"document.getElementById('modal-schemes').style.display='flex'; return false;\""
)

content = content.replace(
    "onclick=\"showNotification('Downloading Pune District Education Directory PDF...', 'success'); return false;\"",
    "onclick=\"document.getElementById('modal-edu').style.display='flex'; return false;\""
)

content = content.replace(
    "onclick=\"showNotification('Searching for verified NGO support groups near your GPS location...', 'success'); return false;\"",
    "onclick=\"document.getElementById('modal-ngo').style.display='flex'; return false;\""
)

# Modals HTML
modals = """
        <!-- Mock Data Modals -->
        <style>
            .data-modal {
                display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                background: rgba(0,0,0,0.6); z-index: 9999; justify-content: center; align-items: center;
                backdrop-filter: blur(4px);
            }
            .data-modal-content {
                background: var(--bg-surface); padding: 30px; border-radius: 12px; width: 90%; max-width: 600px;
                max-height: 80vh; overflow-y: auto; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
            }
            .data-modal .close {
                position: absolute; top: 15px; right: 20px; font-size: 1.5rem; cursor: pointer; color: var(--text-muted);
            }
            .data-item {
                border-bottom: 1px solid var(--border-light); padding: 15px 0; display: flex; justify-content: space-between; align-items: center; gap: 15px;
            }
            .data-item:last-child { border-bottom: none; }
            .data-item h4 { margin: 0 0 5px; color: var(--brand-blue); }
            .data-item p { margin: 0; font-size: 0.9rem; color: var(--text-main); }
        </style>

        <div id="modal-schemes" class="data-modal">
            <div class="data-modal-content">
                <span class="close" onclick="document.getElementById('modal-schemes').style.display='none'">&times;</span>
                <h2 style="margin-top: 0;">Government Schemes Database</h2>
                <div class="data-item">
                    <div>
                        <h4>Niramaya Health Insurance</h4>
                        <p>Affordable health insurance scheme covering up to Rs. 1.0 Lakh for therapies and medical interventions.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Redirecting to National Trust...', 'success')">Apply</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>Deendayal Disabled Rehabilitation</h4>
                        <p>Financial assistance to NGOs for providing vocational training and rehabilitation services.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Downloading PDF...', 'success')">Details</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>State Transport Concession Pass</h4>
                        <p>75% concession in bus fares for persons with 40%+ disability in Maharashtra State Transport.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Opening RTO Portal...', 'success')">Apply</button>
                </div>
            </div>
        </div>

        <div id="modal-edu" class="data-modal">
            <div class="data-modal-content">
                <span class="close" onclick="document.getElementById('modal-edu').style.display='none'">&times;</span>
                <h2 style="margin-top: 0;">Educational Directory (Pune)</h2>
                <div class="data-item">
                    <div>
                        <h4>Sweekar Special School</h4>
                        <p>Deccan Gymkhana. Specializes in autism and intellectual disabilities. Grades 1-10.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Calling +91 9876543210...', 'success')">Contact</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>SkillHub Vocational Center</h4>
                        <p>Kothrud. Computer literacy and data entry training tailored for visually impaired students.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Opening Maps...', 'success')">Map</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>National Fellowship (UGC)</h4>
                        <p>Higher education scholarship providing Rs. 31,000/month for M.Phil and Ph.D students.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Opening UGC Portal...', 'success')">Portal</button>
                </div>
            </div>
        </div>

        <div id="modal-ngo" class="data-modal">
            <div class="data-modal-content">
                <span class="close" onclick="document.getElementById('modal-ngo').style.display='none'">&times;</span>
                <h2 style="margin-top: 0;">Verified Support Networks</h2>
                <div class="data-item">
                    <div>
                        <h4>Pune Deaf Association</h4>
                        <p>Shivajinagar. Weekly sign language workshops and employment counseling.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Opening Website...', 'success')">Visit</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>CareGivers Alliance</h4>
                        <p>Aundh. Fortnightly support groups and mental health counseling for parents and caretakers.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Booking Session...', 'success')">Join</button>
                </div>
                <div class="data-item">
                    <div>
                        <h4>Free Mobility Camp (Upcoming)</h4>
                        <p>Sassoon Hospital. Free assessment for prosthetics and wheelchairs. 25th September.</p>
                    </div>
                    <button class="btn secondary" style="white-space: nowrap;" onclick="showNotification('Registering...', 'success')">Register</button>
                </div>
            </div>
        </div>
"""

content = content.replace('</main>', modals + '\n    </main>')

with open('templates/resources.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modals injected.")
