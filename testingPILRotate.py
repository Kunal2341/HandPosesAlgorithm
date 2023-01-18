from PIL import Image, ImageDraw
import math

def rotate_point(x, y, width, height):
    radians = math.radians(45)  # convert degrees to radians
    new_x = (x - 0.5) * math.cos(radians) - (y - 0.5) * math.sin(radians) + 0.5
    new_y = (x - 0.5) * math.sin(radians) + (y - 0.5) * math.cos(radians) + 0.5
    return new_x * width, new_y * height

x = 0.67807657
y = 0.20800887
width = 1920
height = 1080
rotated_x, rotated_y = rotate_point(x, y, width, height)
origin_x,origin_y = x*width, y*height

# create a new image and draw the rotated point on it
image = Image.new("RGB", (width, height), (255, 255, 255))
image = Image.open("009.jpg")
draw = ImageDraw.Draw(image)

# increase the size of the point
size = 25
draw.ellipse((rotated_x-size, rotated_y-size, rotated_x+size, rotated_y+size), fill=(0, 0, 255))
draw.ellipse((origin_x-size, origin_y-size, origin_x+size, origin_y+size), fill=(255, 0, 0))

# display the image
image.save("a.png")
