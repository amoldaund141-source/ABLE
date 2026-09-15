with open('static/styles.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Toggle Switch CSS */
.switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}
.switch input { 
  opacity: 0;
  width: 0;
  height: 0;
}
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #cbd5e1;
  transition: .4s;
}
.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
}
input:checked + .slider {
  background-color: #2563eb;
}
input:focus + .slider {
  box-shadow: 0 0 1px #2563eb;
}
input:checked + .slider:before {
  transform: translateX(26px);
}
.slider.round {
  border-radius: 24px;
}
.slider.round:before {
  border-radius: 50%;
}
body.dark-mode .slider {
  background-color: #334155;
}
body.dark-mode input:checked + .slider {
  background-color: #3b82f6;
}
''')
