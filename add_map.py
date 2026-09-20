import re

with open('templates/volunteer-requests.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hardcoded cards with a map container and a list container
new_layout = """                <div id="tab-nearby" class="vol-tab">
                    <h2 style="margin-bottom: 20px;">Urgent Nearby Requests</h2>
                    
                    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px; margin-bottom: 30px;">
                        <!-- Map Container -->
                        <div class="card" style="padding: 0; overflow: hidden; height: 500px; position: relative;">
                            <div id="volunteer-map" style="width: 100%; height: 100%; z-index: 1;"></div>
                        </div>
                        
                        <!-- List Container -->
                        <div class="card" style="overflow-y: auto; height: 500px;" id="live-requests-list">
                            <h3 style="margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid var(--border-light);">Live Feed</h3>
                            <div id="live-requests-feed">
                                <p style="text-align: center; color: var(--text-muted); margin-top: 50px;">Loading requests from database...</p>
                            </div>
                        </div>
                    </div>
                </div>"""

# Match everything from <div id="tab-nearby"... down to the end of the cards before tab-history
html = re.sub(r'<div id="tab-nearby" class="vol-tab">.*?<div id="tab-history"', new_layout + '\n\n                <div id="tab-history"', html, flags=re.DOTALL)

# Add Leaflet CSS and JS to the head
leaflet_assets = """    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>"""
html = html.replace('    <link rel="stylesheet" href="styles.css">', leaflet_assets)

with open('templates/volunteer-requests.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added map container to volunteer-requests.html!")
