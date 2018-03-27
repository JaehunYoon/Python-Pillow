from PIL import Image, ImageDraw

width, height = map(int, input("Please input width and height > ").split())
new = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(new)

r = 0
g = 0
b = 0

for i in range(0, height):
    draw.line((0, i) + (width, i), (r, g, b))
    r += 1
    g += 1
    b += 1
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
new.save('02_gradient.png')
