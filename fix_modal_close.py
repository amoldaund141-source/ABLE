import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_func = re.search(r'window\.showNotification = function\(.*?\).*?modal\.style\.display = \'block\';\s*\}', text, re.DOTALL)
if old_func:
    new_func = '''window.closeNotification = function() {
    let modal = document.getElementById('form-modal');
    let overlay = document.getElementById('form-overlay');
    if (modal) modal.style.display = 'none';
    if (overlay) overlay.style.display = 'none';
};

window.showNotification = function(title, text, icon="check_circle", color="#10b981") {
            let modal = document.getElementById('form-modal');
            if (!modal) {
                document.body.insertAdjacentHTML('beforeend', `
                    <div id="form-overlay" onclick="closeNotification()" style="position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; display:none; cursor:pointer;"></div>
                    <div id="form-modal" style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); background:var(--bg-surface, #ffffff); color:var(--text-main, #333333); padding:30px; border-radius:12px; z-index:10000; display:none; max-width:400px; width:90%; box-shadow:0 10px 25px rgba(0,0,0,0.2); text-align:center;">
                        <span id="form-modal-icon" class="material-symbols-outlined" style="font-size:4rem; margin-bottom:15px; display:block;"></span>
                        <h3 id="form-modal-title" style="margin-bottom:10px; font-size:1.5rem;"></h3>
                        <p id="form-modal-text" style="color:var(--text-muted, #666666); margin-bottom:20px; line-height:1.5;"></p>
                        <button type="button" class="btn" style="width:100%;" onclick="closeNotification()">Close</button>
                    </div>
                `);
                modal = document.getElementById('form-modal');
            }
            
            document.getElementById('form-modal-title').innerText = title;
            document.getElementById('form-modal-text').innerText = text;
            document.getElementById('form-modal-icon').innerText = icon;
            document.getElementById('form-modal-icon').style.color = color;
            
            document.getElementById('form-overlay').style.display = 'block';
            modal.style.display = 'block';
        }'''
    
    text = text[:old_func.start()] + new_func + text[old_func.end():]
    with open('static/script.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated showNotification')
else:
    print('Could not find showNotification in script.js')
