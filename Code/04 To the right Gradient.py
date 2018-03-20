from PIL import Image, ImageDraw

width, height = input("Please input width and height > ").split()
width = int(width)
height = int(height)
new = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(new)

r = 0
g = 0
b = 0

for i in range(0, width):
    draw.line((i, 0) + (i, height), (int(r), int(g), int(b)))
    r += 255 / width
    g += 255 / width
    b += 255 / width
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
new.save('04_gradient.png')
