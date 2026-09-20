with open('static/styles.css', 'a', encoding='utf-8') as f:
    f.write('''

/* Fix for checkboxes and radio buttons which were incorrectly inheriting width: 100% */
input[type="checkbox"], input[type="radio"] {
  width: auto;
  padding: 0;
  margin-right: 10px;
  display: inline-block;
  vertical-align: middle;
  cursor: pointer;
}

/* Ensure labels wrapping checkboxes align items properly */
label:has(input[type="checkbox"]), label:has(input[type="radio"]) {
  display: flex !important;
  align-items: center;
  font-weight: 400 !important;
  cursor: pointer;
}
''')
print("Fixed CSS for checkboxes!")
