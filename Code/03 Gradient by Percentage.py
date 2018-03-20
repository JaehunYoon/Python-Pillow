from PIL import Image, ImageDraw

width, height = input("Please input width and height > ").split()
width = int(width)
height = int(height)
new = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(new)

r = 0
g = 0
b = 0

for i in range(0, height):
    draw.line((0, i) + (width, i), (int(r), int(g), int(b)))
    r += 255 / height
    g += 255 / height
    b += 255 / height
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
new.save('03_gradient.png')
