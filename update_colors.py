import sys

def update_html():
    file_path = "c:\\Users\\Anonimo\\Documents\\Work\\CAS\\cas.html"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as f:
            content = f.read()

    # CSS Tokens update
    content = content.replace("--teal:      #1d4a42;", "--teal:      #2f5c5f;")
    content = content.replace("--teal-mid:  #2a6659;", "--teal-mid:  #3d767a;")
    content = content.replace("--teal-lt:   #3d8c7a;", "--teal-lt:   #529da1;")
    content = content.replace("--teal-pale: #eaf3f1;", "--teal-pale: #ebf2f2;")
    content = content.replace("--teal-pale2:#d4ebe6;", "--teal-pale2:#d5e5e6;")
    content = content.replace("--accent:    #1d4a42;", "--accent:    #2f5c5f;")
    content = content.replace("--border2:   rgba(29,74,66,.18);", "--border2:   rgba(47,92,95,.18);")

    # Other css colors
    content = content.replace("rgba(29,74,66", "rgba(47,92,95")
    content = content.replace("background:#2a7a5a;", "background:#3d767a;")
    content = content.replace("color:#2a7a5a", "color:#3d767a")

    # Logo injection
    logo_css = ".logo-image{height:36px;width:auto;object-fit:contain;}"
    if ".logo-image" not in content:
        content = content.replace(".logo-mark{", logo_css + "\n.logo-mark{")
    
    content = content.replace('<div class="logo-mark">CAS</div>', '<img src="logo.png" alt="CAS Logo" class="logo-image">')

    # Footer logo tweaks
    content = content.replace(".footer-brand .logo-mark{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);margin-bottom:14px}", ".footer-brand .logo-image{margin-bottom:14px; opacity:0.9;}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated colors and logo successfully.")

if __name__ == "__main__":
    update_html()
