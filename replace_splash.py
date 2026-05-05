import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
old_css = """    /* SPLASH */
    #splash {
      background: linear-gradient(160deg, #001a5c 0%, #003087 60%, #0050c8 100%);
      align-items: center;
      justify-content: center;
      gap: 28px
    }"""
new_css = """    /* SPLASH */
    #splash {
      position: relative;
      align-items: center;
      justify-content: center;
      gap: 20px;
      overflow: hidden;
    }
    .splash-bg {
      position: absolute;
      inset: 0;
      background-image: url('college.jpg');
      background-size: cover;
      background-position: center;
      filter: brightness(0.45);
      z-index: 0;
    }
    .splash-content {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 18px;
    }
    .splash-college-logo {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: white;
      padding: 10px;
      object-fit: contain;
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .splash-college-name {
      color: #ffffff;
      font-size: 18px;
      font-weight: 800;
      font-family: 'Poppins', sans-serif;
      text-align: center;
      text-shadow: 0 2px 8px rgba(0,0,0,0.5);
      padding: 0 24px;
      line-height: 1.4;
    }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced CSS.")
else:
    print("Could not find CSS block. Trying flexible match...")
    css_pattern = r'/\* SPLASH \*/\s*#splash\s*\{[^}]*\}'
    new_content, count = re.subn(css_pattern, new_css, content)
    if count > 0:
        content = new_content
        print("Replaced CSS via regex.")
    else:
        print("CSS regex also failed.")

# Replace HTML
html_pattern = r'(<div id="splash" class="screen active">).*?(</div>\s+<!-- LOGIN -->)'
html_replacement = r'\1\n      <div class="splash-bg"></div>\n      <div class="splash-content">\n        <img src="logo.png" alt="GGCT Logo" class="splash-college-logo" />\n        <div class="splash-college-name">Gyan Ganga College of Technology</div>\n        <div class="splash-dots">\n          <div class="dot"></div>\n          <div class="dot"></div>\n          <div class="dot"></div>\n        </div>\n      </div>\n    \2'

new_content, count = re.subn(html_pattern, html_replacement, content, flags=re.DOTALL)
if count > 0:
    content = new_content
    print("Replaced HTML.")
else:
    print("Could not find HTML block.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved.")
