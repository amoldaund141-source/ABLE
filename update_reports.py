import glob, re

mock_1 = "<div style='text-align:left; background:var(--bg-page); padding:15px; border-radius:8px; margin-top:15px; border:1px solid var(--border-light); font-size:0.95rem;'><p style='margin-bottom:8px;'><strong>Reporter:</strong> Rahul S.</p><p style='margin-bottom:8px;'><strong>Location:</strong> Deccan Gymkhana (Lat: 18.515, Lng: 73.840)</p><p style='margin-bottom:8px;'><strong>Issue:</strong> Broken Wheelchair Ramp at main entrance. Completely inaccessible for wheelchair users.</p><p style='margin-bottom:8px;'><strong>Severity:</strong> <span style='color:#ef4444; font-weight:bold;'>High</span></p><p style='margin:0;'><strong>Status:</strong> <span style='color:#f59e0b;'>Investigating (Assigned to PMC Ward Officer)</span></p></div>"

mock_2 = "<div style='text-align:left; background:var(--bg-page); padding:15px; border-radius:8px; margin-top:15px; border:1px solid var(--border-light); font-size:0.95rem;'><p style='margin-bottom:8px;'><strong>Reporter:</strong> Priya M.</p><p style='margin-bottom:8px;'><strong>Location:</strong> Shivaji Nagar Station (Platform 1)</p><p style='margin-bottom:8px;'><strong>Issue:</strong> Elevator Out of Order. Doors are jammed.</p><p style='margin-bottom:8px;'><strong>Severity:</strong> <span style='color:#ef4444; font-weight:bold;'>High</span></p><p style='margin:0;'><strong>Status:</strong> <span style='color:#10b981;'>Repair Dispatched (ETA: 2 hours)</span></p></div>"

mock_3 = "<div style='text-align:left; background:var(--bg-page); padding:15px; border-radius:8px; margin-top:15px; border:1px solid var(--border-light); font-size:0.95rem;'><p style='margin-bottom:8px;'><strong>Reporter:</strong> Anonymous</p><p style='margin-bottom:8px;'><strong>Location:</strong> FC Road (Near Vaishali)</p><p style='margin-bottom:8px;'><strong>Issue:</strong> Obstructed Tactile Path due to illegal vendor cart.</p><p style='margin-bottom:8px;'><strong>Severity:</strong> <span style='color:#f59e0b; font-weight:bold;'>Medium</span></p><p style='margin:0;'><strong>Status:</strong> <span style='color:#64748b;'>Resolved (Cleared by Anti-Encroachment Squad)</span></p></div>"

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Add Action header
    html = html.replace("<th>Severity</th>\n                                      <th>Status</th>\n                                  </tr>", "<th>Severity</th>\n                                      <th>Status</th>\n                                      <th>Action</th>\n                                  </tr>")
    
    # Row 1
    html = html.replace("<td><span class=\"status-badge status-pending\">Investigating</span></td>\n                                  </tr>", f"<td><span class=\"status-badge status-pending\">Investigating</span></td>\n                                      <td><button class=\"btn secondary\" style=\"padding: 6px 12px; font-size: 0.85rem;\" onclick=\"showNotification('Barrier Report #201', `{mock_1}`, 'visibility', '#3b82f6')\">View</button></td>\n                                  </tr>")
    
    # Row 2
    html = html.replace("<td><span class=\"status-badge status-active\">Repair Dispatched</span></td>\n                                  </tr>", f"<td><span class=\"status-badge status-active\">Repair Dispatched</span></td>\n                                      <td><button class=\"btn secondary\" style=\"padding: 6px 12px; font-size: 0.85rem;\" onclick=\"showNotification('Barrier Report #200', `{mock_2}`, 'visibility', '#3b82f6')\">View</button></td>\n                                  </tr>")
    
    # Row 3
    html = html.replace("<td><span class=\"status-badge status-resolved\">Resolved</span></td>\n                                  </tr>", f"<td><span class=\"status-badge status-resolved\">Resolved</span></td>\n                                      <td><button class=\"btn secondary\" style=\"padding: 6px 12px; font-size: 0.85rem;\" onclick=\"showNotification('Barrier Report #199', `{mock_3}`, 'visibility', '#3b82f6')\">View</button></td>\n                                  </tr>")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print('Updated reports table!')
