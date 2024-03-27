from PIL import Image

with Image.open("./dolls.jpg") as img:
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = r ^ 1
            g = g ^ 1
            b = b ^ 1
            pixels[x, y] = (r, g, b)
    img.save('reversed_lsb.png')