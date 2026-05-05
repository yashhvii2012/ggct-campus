import sys
import os

b64_file = 'logo_b64.txt'
html_file = 'ggct_campus.html'

with open(b64_file, 'r', encoding='utf-8') as f:
    b64 = f.read().strip()

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

splash_svg = """    <svg class="splash-logo-svg" viewBox="0 0 52 52">
      <defs><radialGradient id="g1" cx="50%" cy="50%"><stop offset="0%" stop-color="#0050c8"/><stop offset="100%" stop-color="#001a5c"/></radialGradient></defs>
      <circle cx="26" cy="26" r="26" fill="url(#g1)"/>
      <circle cx="26" cy="26" r="20" fill="none" stroke="#FFB800" stroke-width="2.5"/>
      <circle cx="26" cy="26" r="9" fill="#FFB800"/>
      <line x1="26" y1="6" x2="26" y2="46" stroke="#FFB800" stroke-width="1.5" opacity=".4"/>
      <line x1="6" y1="26" x2="46" y2="26" stroke="#FFB800" stroke-width="1.5" opacity=".4"/>
      <line x1="12" y1="12" x2="40" y2="40" stroke="#FFB800" stroke-width="1" opacity=".25"/>
      <line x1="40" y1="12" x2="12" y2="40" stroke="#FFB800" stroke-width="1" opacity=".25"/>
    </svg>"""

login_svg = """      <svg width="38" height="38" viewBox="0 0 52 52">
        <circle cx="26" cy="26" r="26" fill="#003087"/>
        <circle cx="26" cy="26" r="20" fill="none" stroke="#FFB800" stroke-width="2.5"/>
        <circle cx="26" cy="26" r="9" fill="#FFB800"/>
      </svg>"""

dropdown = """      <select id="branch-sel">
        <option value="">-- Select Branch --</option>
        <optgroup label="B.E. / B.Tech">
          <option>Computer Science Engineering (CSE)</option>
          <option>Information Technology (IT)</option>
          <option>Electronics &amp; Communication (EC)</option>
          <option>Electrical Engineering (EE)</option>
          <option>Mechanical Engineering (ME)</option>
          <option>Civil Engineering (CE)</option>
        </optgroup>
        <optgroup label="PG Programs">
          <option>MBA</option><option>MCA</option><option>M.Tech (CSE)</option><option>M.Tech (EC)</option>
        </optgroup>
        <optgroup label="Pharmacy">
          <option>B.Pharm</option><option>M.Pharm</option>
        </optgroup>
        <optgroup label="Diploma">
          <option>Diploma – Computer Science</option><option>Diploma – Mechanical</option><option>Diploma – Civil</option>
        </optgroup>
      </select>"""

splash_img = f'    <img src="data:image/png;base64,{b64}" alt="GGCT Logo" style="width: 52px; height: 52px; object-fit: contain;">'
login_img = f'      <img src="data:image/png;base64,{b64}" alt="GGCT Logo" style="width: 38px; height: 38px; object-fit: contain;">'

new_dropdown = """      <select id="branch-sel">
        <option value="">-- Select Branch --</option>
        <optgroup label="B.Tech">
          <option>Computer Science Engineering (CSE)</option>
          <option>CSE – AI &amp; Data Science (AIDS)</option>
          <option>CSE – AI &amp; Machine Learning (AIML)</option>
        </optgroup>
      </select>"""

# Normalize line endings to avoid matching issues
content = content.replace('\\r\\n', '\\n')
splash_svg = splash_svg.replace('\\r\\n', '\\n')
login_svg = login_svg.replace('\\r\\n', '\\n')
dropdown = dropdown.replace('\\r\\n', '\\n')

if splash_svg in content:
    content = content.replace(splash_svg, splash_img)
    print("Replaced splash_svg")
else:
    print("Splash SVG not found")

if login_svg in content:
    content = content.replace(login_svg, login_img)
    print("Replaced login_svg")
else:
    print("Login SVG not found")

if dropdown in content:
    content = content.replace(dropdown, new_dropdown)
    print("Replaced dropdown")
else:
    print("Dropdown not found")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
