from PIL import Image, ImageChops
import sys

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

if __name__ == "__main__":
    im = Image.open('Screenshot 2026-03-22 211011.png')
    im = trim(im)
    im.save('logo.png')
    print("Cropped logo saved to logo.png")
