from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (255, 255, 255))

draw = ImageDraw.Draw(img)

draw.polygon([(50, 0), (100, 100), (0, 100)], (255, 0, 0, 125))
draw.polygon([(50, 100), (100, 0), (0, 0)], (0, 255, 0, 125))

del draw

img.show()
