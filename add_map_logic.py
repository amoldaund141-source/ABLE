with open('static/script.js', 'a', encoding='utf-8') as f:
    f.write('''

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
''')
print("Added Leaflet map logic!")
