import glob
import re

mega_footer = """
    <!-- Professional Mega Footer -->
    <footer class="org-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h2>ABLE</h2>
                    <p>Awareness • Accessibility • Inclusion</p>
                    <p style="font-size: 0.9rem; margin-top: 15px;">A community-focused digital platform engineered to resolve information gaps and physical barriers for Persons with Disabilities.</p>
                </div>
                <div class="footer-links">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="awareness.html">Disability Awareness</a></li>
                        <li><a href="resources.html">Government Schemes</a></li>
                        <li><a href="report.html">Report a Barrier</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h3>Contact Us</h3>
                    <p><span class="material-symbols-outlined" style="font-size: 1rem; vertical-align: middle;">location_on</span> Shivajinagar, Pune 411005</p>
                    <p><span class="material-symbols-outlined" style="font-size: 1rem; vertical-align: middle;">mail</span> support@able-portal.org</p>
                    <p><span class="material-symbols-outlined" style="font-size: 1rem; vertical-align: middle;">call</span> +91 800-123-4567</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 ABLE Community Engagement Project. Developed by Department of Computer Engineering.</p>
            </div>
        </div>
    </footer>
"""

files = glob.glob('*.html')
files.remove('index.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace plain footer with mega footer
    content = re.sub(r'<footer>.*?</footer>', mega_footer.strip(), content, flags=re.DOTALL)
    
    # Extract h1 and first p inside main > section to create page header
    match = re.search(r'<main>\s*<section>\s*<h1>(.*?)</h1>\s*<p>(.*?)</p>', content, flags=re.DOTALL)
    
    if match:
        h1_text = match.group(1)
        p_text = match.group(2)
        
        replacement = f"""<main>
        <section class="page-header">
            <div class="page-header-content">
                <h1>{h1_text}</h1>
                <p>{p_text}</p>
            </div>
        </section>
        <section>"""
        
        content = content[:match.start()] + replacement + content[match.end():]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Internal pages upgraded with page headers and mega footer.")
