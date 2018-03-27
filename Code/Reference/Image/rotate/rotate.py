from PIL import Image  # Add Pillow library

draw = Image.open("exam.png")  # Open image file
draw.rotate(45).show()  # Rotate 45 degrees

# .show() => Display image file directly without saving.
