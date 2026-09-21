import glob
import re

files = glob.glob('templates/admin*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We replace the static Sneha Sharma table body with <tbody id="admin-volunteers-tbody"></tbody>
    pattern = r'                                  <thead>\s*<tr>\s*<th>Name</th>\s*<th>Email</th>\s*<th>Affiliation</th>\s*<th>Contribution Role</th>\s*<th>Action</th>\s*</tr>\s*</thead>\s*<tbody>.*?</tbody>'
    
    replacement = """                                  <thead>
                                      <tr>
                                          <th>Name</th>
                                          <th>Email</th>
                                          <th>Affiliation</th>
                                          <th>Contribution Role</th>
                                          <th>Action</th>
                                      </tr>
                                  </thead>
                                  <tbody id="admin-volunteers-tbody">
                                      <!-- Dynamically populated -->
                                  </tbody>"""
    
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated admin HTML files to use dynamic volunteer tbody.")
