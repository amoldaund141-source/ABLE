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
                <li><a href="admin.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> Dashboard</a></li>
                <li><a href="#"><span class="material-symbols-outlined" style="vertical-align: middle;">inbox</span> All Requests</a></li>
                <li><a href="#"><span class="material-symbols-outlined" style="vertical-align: middle;">group</span> Volunteers</a></li>
                <li><a href="#"><span class="material-symbols-outlined" style="vertical-align: middle;">analytics</span> Reports</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
            `;
        } else if (userRole === 'volunteer') {
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="volunteer-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> My Dashboard</a></li>
                <li><a href="#"><span class="material-symbols-outlined" style="vertical-align: middle;">map</span> Available Requests</a></li>
                <li><a href="#"><span class="material-symbols-outlined" style="vertical-align: middle;">history</span> History</a></li>
                <li><a href="#" onclick="localStorage.clear(); window.location.href='index.html';" style="color: #dc2626;"><span class="material-symbols-outlined" style="vertical-align: middle;">logout</span> Logout</a></li>
            `;
        } else {
            // Standard Citizen/Beneficiary
            navUl.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="user-dashboard.html"><span class="material-symbols-outlined" style="vertical-align: middle;">dashboard</span> Dashboard</a></li>
                <li><a href="assistance.html"><span class="material-symbols-outlined" style="vertical-align: middle;">health_and_safety</span> Request Help</a></li>
                <li><a href="report.html"><span class="material-symbols-outlined" style="vertical-align: middle;">report</span> Report Barrier</a></li>
                <li><a href="accessibility.html"><span class="material-symbols-outlined" style="vertical-align: middle;">accessible</span> Directory Map</a></li>
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
            document.getElementById('form-modal').classList.remove('active');
            document.getElementById('form-overlay').classList.remove('active');
        }
        
        window.showNotification = function(title, text, icon="check_circle", color="#10b981") {
            document.getElementById('form-modal-title').innerText = title;
            document.getElementById('form-modal-text').innerText = text;
            document.getElementById('form-modal-icon').innerText = icon;
            document.getElementById('form-modal-icon').style.color = color;
            document.getElementById('form-modal').classList.add('active');
            document.getElementById('form-overlay').classList.add('active');
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
        <!-- Emergency SOS Button -->
        <div id="sos-btn" style="position: fixed; bottom: 30px; left: 30px; background-color: #dc2626; color: white; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(220, 38, 38, 0.5); cursor: pointer; z-index: 1000; transition: transform 0.3s; animation: pulse 2s infinite;">
            <span class="material-symbols-outlined" style="font-size: 2.2rem;">sos</span>
        </div>

        <!-- SOS Cancel Modal -->
        <div class="mock-modal" id="sos-modal">
            <span class="material-symbols-outlined" style="font-size: 3rem; color: #dc2626; margin-bottom: 15px;">warning</span>
            <h3 style="margin-bottom: 10px; color: #dc2626;">EMERGENCY SOS TRIGGERED</h3>
            <p>Dispatching emergency services to your location in <strong id="sos-timer" style="font-size: 1.5rem;">5</strong> seconds.</p>
            <button class="btn secondary" style="margin-top: 20px; border-color: #dc2626; color: #dc2626; width: 100%;" onclick="cancelSOS()">CANCEL SOS</button>
        </div>

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

    // SOS Logic
    let sosInterval;
    document.getElementById('sos-btn').addEventListener('click', () => {
        let timer = 5;
        document.getElementById('sos-timer').innerText = timer;
        document.getElementById('sos-modal').classList.add('active');
        document.getElementById('form-overlay').classList.add('active');
        
        sosInterval = setInterval(() => {
            timer--;
            document.getElementById('sos-timer').innerText = timer;
            if(timer <= 0) {
                clearInterval(sosInterval);
                document.getElementById('sos-modal').innerHTML = `
                    <span class="material-symbols-outlined" style="font-size: 3rem; color: #16a34a; margin-bottom: 15px;">local_police</span>
                    <h3 style="margin-bottom: 10px;">SOS DISPATCHED</h3>
                    <p>Emergency responders and nearby NSS volunteers have been alerted with your live GPS location.</p>
                    <button class="btn" style="margin-top: 20px;" onclick="closeModal(); location.reload();">Close</button>
                `;
            }
        }, 1000);
    });

    window.cancelSOS = function() {
        clearInterval(sosInterval);
        closeModal();
    }

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
        "Accessibility": "प्रवेशयोग्यता",
        "Resources": "संसाधने",
        "Assistance": "मदत",
        "Volunteer": "स्वयंसेवक",
        "Report": "अहवाल",
        "Login": "लॉगिन",
        "Dashboard": "डॅशबोर्ड",
        "Logout": "बाहेर पडा",
        "Report a Barrier": "अडथळा नोंदवा",
        "Request Help": "मदत मागा",
        "All Requests": "सर्व विनंत्या",
        "My Dashboard": "माझा डॅशबोर्ड",
        "History": "इतिहास"
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
        const elementsToTranslate = document.querySelectorAll('a, button, h1, h2, h3, th');
        
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
                document.getElementById('lang-text').innerText = 'English';
            } else {
                currentLang = 'en';
                document.getElementById('lang-text').innerText = 'मराठी';
            }
            localStorage.setItem('able_lang', currentLang);
            applyTranslations();
        });
    }

});
