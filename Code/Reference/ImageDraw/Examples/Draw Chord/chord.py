from PIL import Image, ImageDraw

width, height = map(int, input("please input width, height value >> ").split())

img = Image.new('RGBA', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(img)

draw.chord((1, 1, width-1, height-1), 0, end=360, fill='yellow', outline='red')

del draw

img.show()
