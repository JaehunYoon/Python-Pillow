from PIL import Image, ImageDraw

width, height = map(int, input("please input width and height value >> ").split())

img = Image.new('RGBA', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(img)

draw.ellipse((0, 0, width-1, height-1), (255, 255, 0), (0, 0, 0))
draw.ellipse((int(width/3.6), int(height/4.5), int(width/2.57), int(height/3)), (255, 255, 255), (0, 0, 0))
draw.ellipse((int(width/1.8), int(height/4.5), int(width/1.5), int(height/3)), (255, 255, 255), (0, 0, 0))
draw.arc((int(width/4.5), int(width/2.25), int(height/1.3), int(height/1.3)), 0, 180, (0, 0, 0))

del draw

img.show()
