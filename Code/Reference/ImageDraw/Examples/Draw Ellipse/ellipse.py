from PIL import Image, ImageDraw

width, height = map(int, input("please input width, height value >> ").split())

img = Image.new('RGBA', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(img)

for i in range(width, 0, -1):
    draw.ellipse(((0, 0), (width, height)), (0, 255, 255), (0, 0, 0))

del draw

img.show()
