import glob, re

mock_view = "<div style='text-align:left; background:var(--bg-page); padding:15px; border-radius:8px; margin-top:15px; border:1px solid var(--border-light); font-size:0.95rem;'><p style='margin-bottom:8px;'><strong>Name:</strong> Anjali Verma</p><p style='margin-bottom:8px;'><strong>Phone:</strong> +91 98765 43210</p><p style='margin-bottom:8px;'><strong>Location:</strong> Modern College Main Gate (Lat: 18.528, Lng: 73.844)</p><p style='margin-bottom:8px;'><strong>Needs:</strong> Navigation Guide (Visual Impairment)</p><p style='margin-bottom:8px;'><strong>Volunteer:</strong> Sameer Joshi (ETA: 4 mins)</p><p style='margin:0;'><strong>Status:</strong> <span style='color:#10b981;'>Dispatched</span></p></div>"

files = glob.glob('templates/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the broken syntax first
    html = html.replace(f"showNotification('Request #1041 Dossier', \"{mock_view}\", 'visibility', '#3b82f6')", f"showNotification('Request #1041 Dossier', `{mock_view}`, 'visibility', '#3b82f6')")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print('Fixed HTML attribute syntax!')
