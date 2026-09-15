import glob

settings_html = '''
                      <div class="card" style="padding: 30px; margin-top: 20px;">
                          <h4 style="margin-bottom: 15px; border-bottom: 1px solid var(--border-light); padding-bottom: 10px;">Dispatch & Routing Behavior</h4>
                          
                          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                              <div>
                                  <strong>Auto-Dispatch Volunteers</strong>
                                  <p style="font-size: 0.85rem; color: var(--text-muted); margin: 5px 0 0;">Automatically assign new requests to the closest available volunteer.</p>
                              </div>
                              <label class="switch">
                                  <input type="checkbox" checked onchange="showNotification('Setting Saved', 'Auto-dispatch is now active.', 'save', '#3b82f6')">
                                  <span class="slider round"></span>
                              </label>
                          </div>

                          <div style="display: flex; justify-content: space-between; align-items: center;">
                              <div>
                                  <strong>Emergency SMS Broadcasts</strong>
                                  <p style="font-size: 0.85rem; color: var(--text-muted); margin: 5px 0 0;">Send SMS alerts via Twilio for all 'High Severity' barrier reports.</p>
                              </div>
                              <label class="switch">
                                  <input type="checkbox" checked onchange="showNotification('Setting Saved', 'SMS Broadcasts updated.', 'save', '#3b82f6')">
                                  <span class="slider round"></span>
                              </label>
                          </div>
                      </div>

                      <div class="card" style="padding: 30px; margin-top: 20px;">
                          <h4 style="margin-bottom: 15px; border-bottom: 1px solid var(--border-light); padding-bottom: 10px;">System Maintenance</h4>
                          
                          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                              <div>
                                  <strong>Maintenance Mode</strong>
                                  <p style="font-size: 0.85rem; color: var(--text-muted); margin: 5px 0 0;">Disable public access to the portal for backend upgrades.</p>
                              </div>
                              <label class="switch">
                                  <input type="checkbox" onchange="showNotification('Warning', 'System will not enter maintenance mode without admin confirmation.', 'warning', '#f59e0b')">
                                  <span class="slider round"></span>
                              </label>
                          </div>

                          <div style="display: flex; justify-content: space-between; align-items: center;">
                              <div>
                                  <strong>Data Retention Policy</strong>
                                  <p style="font-size: 0.85rem; color: var(--text-muted); margin: 5px 0 0;">How long to keep archived assistance requests.</p>
                              </div>
                              <select class="form-control" style="width: auto; padding: 5px 10px; background: var(--bg-page); color: var(--text-main); border: 1px solid var(--border-light); border-radius: 4px;" onchange="showNotification('Setting Saved', 'Data retention policy updated.', 'save', '#3b82f6')">
                                  <option>30 Days</option>
                                  <option selected>60 Days</option>
                                  <option>90 Days</option>
                                  <option>Indefinite</option>
                              </select>
                          </div>
                      </div>
'''

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We find the end of the first card and inject the new cards before the closing div of tab-settings
    # The first card ends with </div> and then there is </div> (tab-settings end)
    
    # Let's replace the EXACT end of the settings block
    target = '''                          <div style="display: flex; justify-content: space-between;">
                              <span>PostgreSQL Database</span>
                              <span style="color: #10b981; font-weight: bold;">Healthy</span>
                          </div>
                      </div>'''
    
    html = html.replace(target, target + '\n' + settings_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print('Injected new settings!')
