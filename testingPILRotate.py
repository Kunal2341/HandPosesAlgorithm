from PIL import Image, ImageDraw
import math
import os
from io import BytesIO
from pathlib import Path

def rotate_point(x, y, width, height):
    radians = math.radians(45)  # convert degrees to radians
    new_x = (x - 0.5) * math.cos(radians) - (y - 0.5) * math.sin(radians) + 0.5
    new_y = (x - 0.5) * math.sin(radians) + (y - 0.5) * math.cos(radians) + 0.5
    return new_x * width, new_y * height

#{'x': 0.67807657, 'y': 0.20800887, 'z': 5.914594e-08}
#{'x': 0.8323880582867637, 'y': 0.41945024214811816, 'z': 5.914594e-08}

#-----------------------------------------



width = 1920
height = 1080

print(os.getcwd())

mainData = [{'x': 0.67807657, 'y': 0.20800887, 'z': 5.914594e-08}, {'x': 0.6262265, 'y': 0.17171708, 'z': -0.008353886}, {'x': 0.5771074, 'y': 0.16875657, 'z': -0.016691158}, {'x': 0.53960544, 'y': 0.19867118, 'z': -0.022496894}, {'x': 0.5200173, 'y': 0.24284497, 'z': -0.029544042}, {'x': 0.60045314, 'y': 0.1998046, 'z': -0.040305816}, {'x': 0.5561593, 'y': 0.24724272, 'z': -0.055317394}, {'x': 0.5310527, 'y': 0.2762247, 'z': -0.061918586}, {'x': 0.51013184, 'y': 0.2974146, 'z': -0.06583886}, {'x': 0.6218219, 'y': 0.24165823, 'z': -0.042312164}, {'x': 0.57844573, 'y': 0.29860744, 'z': -0.057358146}, {'x': 0.5465466, 'y': 0.3352823, 'z': -0.06409986}, {'x': 0.52153265, 'y': 0.3592567, 'z': -0.07026574}, {'x': 0.63791025, 'y': 0.2769149, 'z': -0.042803846}, {'x': 0.6006995, 'y': 0.33498996, 'z': -0.054603003}, {'x': 0.5707777, 'y': 0.36874065, 'z': -0.05960848}, {'x': 0.54510313, 'y': 0.3890803, 'z': -0.064214505}, {'x': 0.6496781, 'y': 0.30460906, 'z': -0.043253858}, {'x': 0.625367, 'y': 0.36255825, 'z': -0.054052617}, {'x': 0.6050887, 'y': 0.39506626, 'z': -0.059133682}, {'x': 0.58624977, 'y': 0.41754797, 'z': -0.06308594}]
file = "augmentedImgs/rotatedImg-45/001-rotatedImg-45.jpg"
print(file)

# create a new image and draw the rotated point on it
image = Image.new("RGB", (width, height), (255, 255, 255))
#image = Image.open(file)
draw = ImageDraw.Draw(image)
print(image)

import base64

with open(file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
    
with open("image.txt", "w") as text_file:
    text_file.write(encoded_string)



"""
size = 25
for point in mainData:
    rotated_x, rotated_y = rotate_point(point['x'], point['y'], width, height)
    origin_x, origin_y = point['x'] * width, point['x'] * height
    print(rotated_x, rotated_y)
    # increase the size of the point
    draw.ellipse((rotated_x-size, rotated_y-size, rotated_x+size, rotated_y+size), fill=(0, 0, 255))
    draw.ellipse((origin_x-size, origin_y-size, origin_x+size, origin_y+size), fill=(255, 0, 0))

"""
path = Path("output.png")
image.save(path)
print("D")

