import sys
try:
    from PIL import Image
except ImportError:
    print("PIL not found, installing pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def get_dominant_colors(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        # Resize to speed up processing
        img.thumbnail((300, 300))
        colors = img.getcolors(maxcolors=1000000)
        
        if not colors:
            print("Could not get colors.")
            return

        colors = sorted(colors, key=lambda x: x[0], reverse=True)
        print("Potential brand colors:")
        found = 0
        for count, color in colors:
            r, g, b = color
            # Filter out grays, whites, and blacks
            if max(r,g,b) - min(r,g,b) > 20 and sum([r,g,b]) < 700 and sum([r,g,b]) > 50:
                print(f"#{r:02x}{g:02x}{b:02x} (RGB: {r},{g},{b}) - Pixels: {count}")
                found += 1
                if found >= 10:
                    break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_dominant_colors(sys.argv[1])
    else:
        print("Usage: python get_colors.py <image_path>")
