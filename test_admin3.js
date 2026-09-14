
        function switchAdminTab(event, tabId, el) {
            if(event) event.preventDefault();
            console.log("Switching to tab: " + tabId);
            // Remove active class from all links in both menus
            var allLinks = document.querySelectorAll('#admin-menu a, #admin-top-nav a');
            for (var i = 0; i < allLinks.length; i++) {
                allLinks[i].classList.remove('active');
            }
            
            // Add active class to the clicked link
            if (el) {
                el.classList.add('active');
            }

            // Helper to safely add class
            function addActive(selector) {
                var elem = document.querySelector(selector);
                if (elem) elem.classList.add('active');
            }

            // Sync the active class based on the tabId
            if (tabId === 'tab-dashboard') {
                addActive('#admin-menu li:nth-child(1) a');
                addActive('#admin-top-nav li:nth-child(2) a');
            } else if (tabId === 'tab-requests') {
                addActive('#admin-menu li:nth-child(2) a');
                addActive('#admin-top-nav li:nth-child(3) a');
            } else if (tabId === 'tab-reports') {
                addActive('#admin-menu li:nth-child(3) a');
                addActive('#admin-top-nav li:nth-child(5) a');
            } else if (tabId === 'tab-volunteers') {
                addActive('#admin-menu li:nth-child(4) a');
                addActive('#admin-top-nav li:nth-child(4) a');
            } else if (tabId === 'tab-directory') {
                addActive('#admin-menu li:nth-child(5) a');
            } else if (tabId === 'tab-settings') {
                addActive('#admin-menu li:nth-child(6) a');
            }

            // Hide all tabs
            var allTabs = document.querySelectorAll('.admin-tab');
            for (var j = 0; j < allTabs.length; j++) {
                allTabs[j].style.display = 'none';
            }

            // Show selected tab
            var selectedTab = document.getElementById(tabId);
            if (selectedTab) {
                selectedTab.style.display = 'block';
            }
        }
    