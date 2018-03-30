from PIL import Image, ImageDraw, ImageFont

getImage = Image.open('sample.png').convert('RGBA')

text = Image.new('RGBA', getImage.size, (255, 255, 255, 0))

f = ImageFont.truetype('D2coding.ttc', 40)

d = ImageDraw.Draw(text)

d.text((10, 10), "h4lo", font=f, fill=(255, 255, 255, 128))

d.text((10, 60), " :D", font=f, fill=(255, 255, 255, 255))

output = Image.alpha_composite(getImage, text)

output.show()
