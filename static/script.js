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
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
`;
        } else if (userRole === 'volunteer') {
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> My Dashboard</a></li>
                <li><a href="volunteer-requests.html"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Nearby Requests</a></li>
                <li><a href="volunteer-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> My History</a></li>
                <li><a href="volunteer-certificate.html"><span class="material-symbols-outlined" style="vertical-align: middle;">workspace_premium</span> Certificate</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
`;
        } else {
            // Standard Citizen/Beneficiary
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="user-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> Active Requests</a></li>
                <li><a href="user-history.html"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> Past Requests</a></li>
                <li><a href="assistance.html"><span class="material-symbols-outlined" style="vertical-align: middle;">health_and_safety</span> New Request</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
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

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let message = "Your action was saved securely to the database.";
            if (form.id === 'assistance-form') {
                message = "Request saved! An SMS dispatch has been sent via Twilio to 5 registered NSS volunteers in your area.";
            } else if (form.id === 'volunteer-form') {
                message = "Registration complete! Welcome to the team. You will receive an email shortly.";
            } else if (form.id === 'report-form') {
                message = "Barrier report logged into the central database. Thank you for making Pune more accessible!";
            } else if (form.id === 'search-accessibility') {
                showNotification("Scanning...", "Querying OpenStreetMap dataset for verified accessible locations in that area. (Mock Data)", "map", "#3b82f6");
                return;
            }
            
            showNotification("Success!", message);
            form.reset();
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
