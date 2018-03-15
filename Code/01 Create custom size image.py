from PIL import Image, ImageDraw

width, height = input("Please input width and height > ").split()

r, g, b = input("Please input r, g, b value > ").split()

img = Image.new('RGB', (int(width), int(height)), color=(int(r), int(g), int(b)))
draw = ImageDraw.Draw(img)

img.save('01_custom_size_image.png')
