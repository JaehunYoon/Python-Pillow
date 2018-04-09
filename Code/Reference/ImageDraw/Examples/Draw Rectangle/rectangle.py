from PIL import Image, ImageDraw

width, height = map(int, input("please input width, height value >> ").split())

img = Image.new('RGBA', (width, height), 'white')

draw = ImageDraw.Draw(img)

draw.rectangle((width - int(width - 10), height - (height - 10), width - 10, height - 10), fill='skyblue', outline='blue')

del draw

img.show()
