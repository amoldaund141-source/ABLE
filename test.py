
var document = {
    querySelectorAll: function(selector) { return []; },
    querySelector: function(selector) { return null; },
    getElementById: function(id) { return { style: {} }; }
};
function switchAdminTab(tabId, el) {
    var allLinks = document.querySelectorAll('#admin-menu a, #admin-top-nav a');
    for (var i = 0; i < allLinks.length; i++) {
        allLinks[i].classList.remove('active');
    }
    if (el) {
        el.classList.add('active');
    }
    function addActive(selector) {
        var elem = document.querySelector(selector);
        if (elem) elem.classList.add('active');
    }
    if (tabId === 'tab-dashboard') {
        addActive('#admin-menu li:nth-child(1) a');
        addActive('#admin-top-nav li:nth-child(2) a');
    }
    var allTabs = document.querySelectorAll('.admin-tab');
    for (var j = 0; j < allTabs.length; j++) {
        allTabs[j].style.display = 'none';
    }
    var selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.style.display = 'block';
    }
}
switchAdminTab('tab-dashboard', null);
print('JS executes perfectly!')
