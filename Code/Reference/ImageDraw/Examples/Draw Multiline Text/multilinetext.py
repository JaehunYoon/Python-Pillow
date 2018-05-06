from PIL import Image, ImageDraw, ImageFont

getImage = Image.open('sample.png').convert('RGBA')

text = Image.new('RGBA', getImage.size, (255, 255, 255, 0))

f = ImageFont.truetype('D2coding.ttc', 40)

d = ImageDraw.Draw(text)

d.multiline_text((150, 150), "h4lo", font=f, fill=(255, 255, 255, 255) )

output = Image.alpha_composite(getImage, text)

output.show()
