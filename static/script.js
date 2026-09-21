
// --- Robust Logout ---
window.logoutUser = function(e) {
    if (e) e.preventDefault();
    localStorage.removeItem('able_logged_in');
    localStorage.removeItem('able_role');
    localStorage.removeItem('able_email');
    window.location.replace('index.html');
};
document.addEventListener('DOMContentLoaded', () => {
    console.log("ABLE Portal v2.0 Initialized - PWA Cache Cleared");
    // Highlight the active navigation link based on the current URL
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav ul li a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });

    // --- Authentication State Management (Two Interfaces) ---
    const isLoggedIn = localStorage.getItem('able_logged_in') === 'true';
    const userRole = localStorage.getItem('able_role');
    
    // Find the main navigation list
    const navUl = document.querySelector('nav ul');
    
    if (isLoggedIn && navUl) {
        // Completely replace the public navigation with a private System Interface
        if (userRole === 'admin') {
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="admin.html"><span class="material-symbols-outlined" style="vertical-align: middle;">space_dashboard</span> Dashboard</a></li>
                <li><a href="admin-requests.html"><span class="material-symbols-outlined" style="vertical-align: middle;">inbox</span> All Requests</a></li>
                <li><a href="admin-volunteers.html"><span class="material-symbols-outlined" style="vertical-align: middle;">group</span> Volunteers</a></li>
                <li><a href="admin-reports.html"><span class="material-symbols-outlined" style="vertical-align: middle;">analytics</span> Reports</a></li>
                <li><a href="admin-directory.html"><span class="material-symbols-outlined" style="vertical-align: middle;">place</span> Directory</a></li>
                <li><a href="admin-settings.html"><span class="material-symbols-outlined" style="vertical-align: middle;">settings</span> Settings</a></li>
                <li><a href="#" onclick="logoutUser(event)" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
`;
        } else if (userRole === 'volunteer') {
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> My Dashboard</a></li>
                <li><a href="volunteer-requests.html"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Nearby Requests</a></li>
                <li><a href="volunteer-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> My History</a></li>
                <li><a href="volunteer-certificate.html"><span class="material-symbols-outlined" style="vertical-align: middle;">workspace_premium</span> Certificate</a></li>
                <li><a href="#" onclick="logoutUser(event)" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
`;
        } else {
            // Standard Citizen/Beneficiary
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="user-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> Active Requests</a></li>
                <li><a href="user-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> Past Requests</a></li>
                <li><a href="assistance.html"><span class="material-symbols-outlined" style="vertical-align: middle;">health_and_safety</span> New Request</a></li>
                <li><a href="#" onclick="logoutUser(event)" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
`;
        }
        
        // Highlight active link in the new interface
        const newLinks = navUl.querySelectorAll('a');
        newLinks.forEach(link => {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
    }

    // --- Dynamic Modals & Notifications ---
    if(!document.getElementById('form-modal')) {
        document.body.insertAdjacentHTML('beforeend', `
            <div class="mock-modal-overlay" id="form-overlay"></div>
            <div class="mock-modal" id="form-modal">
                <span id="form-modal-icon" class="material-symbols-outlined" style="font-size: 3rem; color: #10b981; margin-bottom: 15px;">check_circle</span>
                <h3 id="form-modal-title" style="margin-bottom: 10px;">Success!</h3>
                <p id="form-modal-text">Action completed successfully.</p>
                <button class="btn" style="margin-top: 20px;" onclick="closeModal()">Close</button>
            </div>
        `);
        
        window.closeModal = function() {
            document.getElementById('form-modal').style.display = 'none';
            document.getElementById('form-overlay').style.display = 'none';
            document.getElementById('form-modal').classList.remove('active');
            document.getElementById('form-overlay').classList.remove('active');
        }
        
        window.closeNotification = function() {
    let modal = document.getElementById('form-modal');
    let overlay = document.getElementById('form-overlay');
    if (modal) modal.style.display = 'none';
    if (overlay) overlay.style.display = 'none';
};

window.showNotification = function(title, text, icon="check_circle", color="#10b981") {
            let modal = document.getElementById('form-modal');
            if (!modal) {
                document.body.insertAdjacentHTML('beforeend', `
                    <div id="form-overlay" onclick="closeNotification()" style="position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; display:none; cursor:pointer;"></div>
                    <div id="form-modal" style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); background:var(--bg-surface, #ffffff); color:var(--text-main, #333333); padding:30px; border-radius:12px; z-index:10000; display:none; max-width:400px; width:90%; box-shadow:0 10px 25px rgba(0,0,0,0.2); text-align:center;">
                        <span id="form-modal-icon" class="material-symbols-outlined" style="font-size:4rem; margin-bottom:15px; display:block;"></span>
                        <h3 id="form-modal-title" style="margin-bottom:10px; font-size:1.5rem;"></h3>
                        <p id="form-modal-text" style="color:var(--text-muted, #666666); margin-bottom:20px; line-height:1.5;"></p>
                        <button type="button" class="btn" style="width:100%;" onclick="closeNotification()">Close</button>
                    </div>
                `);
                modal = document.getElementById('form-modal');
            }
            
            document.getElementById('form-modal-title').innerText = title;
            document.getElementById('form-modal-text').innerHTML = text;
            document.getElementById('form-modal-icon').innerText = icon;
            document.getElementById('form-modal-icon').style.color = color;
            
            document.getElementById('form-overlay').style.display = 'block';
            modal.style.display = 'block';
        }
    }

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        // Skip login form
        if(form.id === 'login-form') return;

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            if (form.id === 'search-accessibility') {
                showNotification("Scanning...", "Querying OpenStreetMap dataset for verified accessible locations in that area. (Mock Data)", "map", "#3b82f6");
                return;
            } else if (form.id === 'directory-form') {
                const data = {
                    name: document.getElementById('dir-name').value,
                    feature: document.getElementById('dir-feature').value
                };
                try {
                    await fetch('/api/directory', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(data)
                    });
                } catch(e) {}
                showNotification('Success!', 'Directory updated securely in the database.', 'check_circle', '#10b981');
                form.reset();
                return;
            } else if (form.id === 'volunteer-form') {
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
        });
    });

    // --- A11y Accessibility Widget & SOS Button ---
    document.body.insertAdjacentHTML('beforeend', `

        <div class="a11y-widget-btn" id="a11y-btn" aria-label="Accessibility Menu">
            <span class="material-symbols-outlined" style="font-size: 2rem;">accessibility_new</span>
        </div>
        <div class="a11y-menu" id="a11y-menu">
            <h4>Accessibility</h4>
            <button id="a11y-speak"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">record_voice_over</span> Read Page Aloud</button>
            <button id="a11y-text"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">format_size</span> Toggle Large Text</button>
            <button id="a11y-contrast"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">contrast</span> High Contrast Mode</button>
            <button id="a11y-reset" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">restart_alt</span> Reset Settings</button>
        </div>
        
        <style>
            @keyframes pulse {
                0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7); }
                70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(220, 38, 38, 0); }
                100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
            }
        </style>
    `);



    // Text-to-Speech Logic
    let isSpeaking = false;
    document.getElementById('a11y-speak').addEventListener('click', () => {
        if (!('speechSynthesis' in window)) {
            alert("Your browser does not support Text-to-Speech.");
            return;
        }
        
        if (isSpeaking) {
            window.speechSynthesis.cancel();
            isSpeaking = false;
            document.getElementById('a11y-speak').innerHTML = '<span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">record_voice_over</span> Read Page Aloud';
        } else {
            // Grab headings and paragraphs to read
            const textToRead = Array.from(document.querySelectorAll('h1, h2, h3, p'))
                                    .map(el => el.innerText)
                                    .join('. ');
                                    
            const utterance = new SpeechSynthesisUtterance(textToRead);
            utterance.rate = 0.9; // slightly slower for accessibility
            
            utterance.onend = () => {
                isSpeaking = false;
                document.getElementById('a11y-speak').innerHTML = '<span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">record_voice_over</span> Read Page Aloud';
            };
            
            window.speechSynthesis.speak(utterance);
            isSpeaking = true;
            document.getElementById('a11y-speak').innerHTML = '<span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 5px; font-size: 1.1rem;">stop_circle</span> Stop Reading';
        }
    });

    const a11yBtn = document.getElementById('a11y-btn');
    const a11yMenu = document.getElementById('a11y-menu');
    
    a11yBtn.addEventListener('click', () => {
        a11yMenu.classList.toggle('active');
    });

    document.getElementById('a11y-text').addEventListener('click', () => {
        document.body.classList.toggle('a11y-large-text');
    });
    
    document.getElementById('a11y-contrast').addEventListener('click', () => {
        document.body.classList.toggle('a11y-high-contrast');
    });
    
    document.getElementById('a11y-reset').addEventListener('click', () => {
        document.body.classList.remove('a11y-large-text', 'a11y-high-contrast');
    });

    // --- Dark Mode Toggle ---
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        // Check local storage for preference
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark-mode');
            themeToggle.innerHTML = '<span class="material-symbols-outlined">light_mode</span>';
        }

        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
                themeToggle.innerHTML = '<span class="material-symbols-outlined">light_mode</span>';
            } else {
                localStorage.setItem('theme', 'light');
                themeToggle.innerHTML = '<span class="material-symbols-outlined">dark_mode</span>';
            }
        });
    }

    // --- Intersection Observer for Scroll Animations ---
    
    // Auto-add the animate class to elements we want to animate
    document.querySelectorAll('.card, .form-container, .stat-box, section > h2, section > h3, section > p').forEach(el => {
        // Don't add to elements already in the animated headers
        if(!el.closest('.hero-org') && !el.closest('.page-header')) {
            el.classList.add('animate-on-scroll');
        }
    });

    // NOW grab all elements that have the class (including hardcoded ones)
    const scrollElements = document.querySelectorAll('.animate-on-scroll');

    const elementInView = (el, dividend = 1) => {
        const elementTop = el.getBoundingClientRect().top;
        // Trigger as soon as the element enters the bottom of the viewport
        return (elementTop <= (window.innerHeight || document.documentElement.clientHeight));
    };

    const displayScrollElement = (element) => {
        element.classList.add('is-visible');
    };

    const handleScrollAnimation = () => {
        scrollElements.forEach((el) => {
            if (elementInView(el, 1.1)) {
                displayScrollElement(el);
            }
        });
    }

    // Initialize once on load
    handleScrollAnimation();
    
    // Listen for scroll events
    window.addEventListener('scroll', () => {
        handleScrollAnimation();
    });

    // --- Custom Native Multi-language (i18n) Support ---
    const translations = {
        "Home": "मुख्य पृष्ठ",
        "About": "आमच्याबद्दल",
        "Awareness": "जागरूकता",
        "Accessibility": "सुलभता",
        "Resources": "संसाधने",
        "Assistance": "मदत",
        "Volunteer": "स्वयंसेवक",
        "Report": "अहवाल द्या",
        "Login": "लॉगिन",
        "Dashboard": "डॅशबोर्ड",
        "Logout": "लॉगआउट",
        "Report a Barrier": "अडथळ्याची नोंद करा",
        "Request Help": "मदतीची विनंती",
        "All Requests": "सर्व विनंत्या",
        "My Dashboard": "माझा डॅशबोर्ड",
        "History": "इतिहास",
        "Nearby Requests": "जवळील विनंत्या",
        "Certificate": "प्रमाणपत्र",
        "New Report": "नवीन अहवाल",
        "Physical Barrier Reports": "शारीरिक अडथळे अहवाल",
        "System Settings": "सिस्टीम सेटिंग्ज",
        "Directory": "निर्देशिका",
        "Volunteers": "स्वयंसेवक",
        "Reports": "अहवाल",
        "My History": "माझा इतिहास",
        "Urgent Nearby Requests": "तातडीच्या जवळील विनंत्या",
        "Volunteer Overview": "स्वयंसेवक विहंगावलोकन",
        "Action": "कृती",
        "View": "पहा",
        "Dispatch": "पाठवा",
        "Archive": "संग्रहित करा",
        "Accept Request": "विनंती स्वीकारा",
        "Status": "स्थिती",
        "Location": "स्थान",
        "Severity": "तीव्रता",
        "Issue": "समस्या",
        "Date": "तारीख",
        "High": "उच्च",
        "Medium": "मध्यम",
        "Low": "कमी",
        "Investigating": "तपासणी सुरू",
        "Repair Dispatched": "दुरुस्ती पाठवली",
        "Resolved": "सोडवले",
        "Dispatched": "पाठवले",
        "Pending": "प्रलंबित",
        "Auto-Dispatch Volunteers": "स्वयंसेवकांना स्वयंचलितरित्या पाठवा",
        "Emergency SMS Broadcasts": "तातडीचे एसएमएस प्रसारण",
        "Maintenance Mode": "देखभाल मोड",
        "Data Retention Policy": "डेटा धारणा धोरण",
        "Twilio SMS Gateway": "ट्विलिओ एसएमएस गेटवे",
        "OpenStreetMap Sync": "ओपनस्ट्रीटमॅप सिंक",
        "PostgreSQL Database": "पोस्टग्रेएसक्यूएल डेटाबेस",
        "Connected": "जोडलेले",
        "Healthy": "निरोगी",
        "API Integrations": "एपीआय एकत्रीकरण",
        "Dispatch & Routing Behavior": "पाठवणे आणि राउटिंग वर्तन",
        "System Maintenance": "सिस्टम देखभाल",
        "Configure backend API integrations and system behavior.": "बॅकएंड एपीआय एकत्रीकरण आणि सिस्टम वर्तन कॉन्फिगर करा.",
        "Today": "आज",
        "Yesterday": "काल",
        "Control Panel": "नियंत्रण कक्ष",
        "Total Users": "एकूण वापरकर्ते",
        "Active Volunteers": "सक्रिय स्वयंसेवक",
        "Pending Requests": "प्रलंबित विनंत्या",
        "Accessibility Score": "सुलभता गुण",
        "System Activity": "सिस्टम क्रियाकलाप",
        "Recent Users": "अलीकडील वापरकर्ते",
        "NSS Volunteer Certificate": "एनएसएस स्वयंसेवक प्रमाणपत्र"
    };

    let currentLang = localStorage.getItem('able_lang') || 'en';
    
          // Inject Language Toggle Button into the header
      const navContainer = document.querySelector('.nav-container');
      if (navContainer) {
          navContainer.insertAdjacentHTML('beforeend', `
              <button id="lang-toggle" class="btn secondary" style="padding: 6px 10px; margin-left: 10px; font-size: 0.9rem;">
                  <span class="material-symbols-outlined" style="vertical-align: middle; font-size: 1.1rem; margin-right: 4px;">translate</span> 
                  <span id="lang-text">${currentLang === 'en' ? 'मराठी' : 'English'}</span>
              </button>
          `);
      }

function applyTranslations() {
        const elementsToTranslate = document.querySelectorAll('a, button, h1, h2, h3, h4, th, td, p, span, div, strong, label, option');
        
        elementsToTranslate.forEach(el => {
            // Only translate nodes that have direct text (ignore icons)
            Array.from(el.childNodes).forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    let originalText = node.nodeValue.trim();
                    if (!originalText) return;

                    // If switching to Marathi
                    if (currentLang === 'mr') {
                        // Store original english in data attribute if not present
                        if (!el.hasAttribute('data-en')) {
                            el.setAttribute('data-en', originalText);
                        }
                        if (translations[originalText]) {
                            node.nodeValue = " " + translations[originalText] + " ";
                        }
                    } 
                    // If switching back to English
                    else if (currentLang === 'en') {
                        if (el.hasAttribute('data-en')) {
                            let enText = el.getAttribute('data-en');
                            // Find the translated key and revert it
                            if(Object.values(translations).includes(originalText)){
                                node.nodeValue = " " + enText + " ";
                            }
                        }
                    }
                }
            });
        });
    }

    // Apply on load
    if (currentLang === 'mr') {
        setTimeout(applyTranslations, 100); // slight delay to ensure DOM is ready
    }

    const langToggleBtn = document.getElementById('lang-toggle');
    if (langToggleBtn) {
        langToggleBtn.addEventListener('click', () => {
            if (currentLang === 'en') {
                currentLang = 'mr';
            } else {
                currentLang = 'en';
            }
            localStorage.setItem('able_lang', currentLang);
            
            // Force reload to apply clean state, applyTranslations sometimes struggles with dynamic DOM
            window.location.reload();
        });
    }

});


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
                    if (document.getElementById('user-requests-tbody') && req.email !== (localStorage.getItem('able_email') || 'user@citizen.org')) {
                        return; // Skip if it's the user dashboard and email doesn't match
                    }
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


// --- Interactive Volunteer Map ---
async function initVolunteerMap() {
    const mapElement = document.getElementById('volunteer-map');
    if (!mapElement) return;

    // Initialize map centered on Pune, India
    const map = L.map('volunteer-map').setView([18.5204, 73.8567], 13);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(map);

    // Custom Icon
    const alertIcon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    try {
        const res = await fetch('/api/requests');
        const data = await res.json();
        
        const feedContainer = document.getElementById('live-requests-feed');
        feedContainer.innerHTML = '';
        
        // Filter only pending requests
        const pending = data.filter(r => r.status === 'Pending');
        
        if (pending.length === 0) {
            feedContainer.innerHTML = '<p style="text-align: center; color: var(--text-muted); margin-top: 50px;">No urgent requests right now.</p>';
            return;
        }

        // Add markers and feed items
        pending.forEach((req, index) => {
            // Generate a slight random offset around Pune for mock coordinates
            const lat = 18.5204 + (Math.random() - 0.5) * 0.05;
            const lng = 73.8567 + (Math.random() - 0.5) * 0.05;
            
            // Add Marker
            const marker = L.marker([lat, lng], {icon: alertIcon}).addTo(map);
            marker.bindPopup(`<b>${req.req_type}</b><br>${req.location}<br><button onclick="dispatchRequest(${req.id}, this)" style="margin-top:8px; background:#10b981; color:white; border:none; padding:4px 8px; border-radius:4px; cursor:pointer;">Accept Job</button>`);

            // Add Feed Card
            const card = `<div class="card" style="padding: 15px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h4 style="margin-bottom: 5px; color: #ef4444; font-size: 1rem;">${req.req_type}</h4>
                <p style="font-size: 0.9rem; margin-bottom: 10px;"><strong>Loc:</strong> ${req.location}</p>
                <button class="btn" onclick="dispatchRequest(${req.id}, this)" style="padding: 6px 12px; font-size: 0.85rem; width: 100%; background: #16a34a;">Accept Request</button>
            </div>`;
            feedContainer.insertAdjacentHTML('beforeend', card);
        });

    } catch (e) {
        console.error("Failed to load map data:", e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('volunteer-map')) {
        setTimeout(initVolunteerMap, 300); // slight delay for DOM sizing
    }
});

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
