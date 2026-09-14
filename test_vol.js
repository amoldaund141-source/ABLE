function switchVolTab(event, tabId, el) {
            if(event) event.preventDefault();
            console.log("Switching to tab: " + tabId);
            var allLinks = document.querySelectorAll('#vol-menu a');
            for (var i = 0; i < allLinks.length; i++) {
                allLinks[i].classList.remove('active');
            }
            if (el) el.classList.add('active');
            
            var allTabs = document.querySelectorAll('.vol-tab');
            for (var j = 0; j < allTabs.length; j++) {
                allTabs[j].style.display = 'none';
            }
            
            var selectedTab = document.getElementById(tabId);
            if (selectedTab) selectedTab.style.display = 'block';
        }
    