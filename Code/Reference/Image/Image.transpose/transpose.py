from PIL import Image

new = Image.open('exam.png')
draw = new.transpose(Image.TRANSPOSE)

draw.show()
