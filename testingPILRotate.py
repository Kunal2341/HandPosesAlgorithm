from PIL import Image, ImageDraw
import math
import os
from io import BytesIO
from pathlib import Path
from pprint import pprint

def rotate_point(x, y, width, height, angle):
    angle = math.radians(angle)
    new_x = (x - width/2) * math.cos(angle) - (y - height/2) * math.sin(angle) + width/2
    new_y = (x - width/2) * math.sin(angle) + (y - height/2) * math.cos(angle) + height/2
    return new_x, new_y

def rotate_point_new(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y
def rotate_point_new(x, y, angle, center_x, center_y):
    angle = math.radians(angle)
    x_temp = x - center_x
    y_temp = y - center_y
    new_x = x_temp * math.cos(angle) - y_temp * math.sin(angle) + center_x
    new_y = x_temp * math.sin(angle) + y_temp * math.cos(angle) + center_y
    return new_x, new_y

def flip_points_horizontally(points_dict):
    for point in points_dict['landmark']:
        point['x'] = 1 - point['x']
    return points_dict

width = 1920
height = 1080

print(os.getcwd())

mainData = [{'x': 0.67807657, 'y': 0.20800887, 'z': 5.914594e-08}, {'x': 0.6262265, 'y': 0.17171708, 'z': -0.008353886}, {'x': 0.5771074, 'y': 0.16875657, 'z': -0.016691158}, {'x': 0.53960544, 'y': 0.19867118, 'z': -0.022496894}, {'x': 0.5200173, 'y': 0.24284497, 'z': -0.029544042}, {'x': 0.60045314, 'y': 0.1998046, 'z': -0.040305816}, {'x': 0.5561593, 'y': 0.24724272, 'z': -0.055317394}, {'x': 0.5310527, 'y': 0.2762247, 'z': -0.061918586}, {'x': 0.51013184, 'y': 0.2974146, 'z': -0.06583886}, {'x': 0.6218219, 'y': 0.24165823, 'z': -0.042312164}, {'x': 0.57844573, 'y': 0.29860744, 'z': -0.057358146}, {'x': 0.5465466, 'y': 0.3352823, 'z': -0.06409986}, {'x': 0.52153265, 'y': 0.3592567, 'z': -0.07026574}, {'x': 0.63791025, 'y': 0.2769149, 'z': -0.042803846}, {'x': 0.6006995, 'y': 0.33498996, 'z': -0.054603003}, {'x': 0.5707777, 'y': 0.36874065, 'z': -0.05960848}, {'x': 0.54510313, 'y': 0.3890803, 'z': -0.064214505}, {'x': 0.6496781, 'y': 0.30460906, 'z': -0.043253858}, {'x': 0.625367, 'y': 0.36255825, 'z': -0.054052617}, {'x': 0.6050887, 'y': 0.39506626, 'z': -0.059133682}, {'x': 0.58624977, 'y': 0.41754797, 'z': -0.06308594}]
handLandMark = {'landmark': [{'x': 0.67807657, 'y': 0.20800887, 'z': 5.914594e-08}, {'x': 0.6262265, 'y': 0.17171708, 'z': -0.008353886}, {'x': 0.5771074, 'y': 0.16875657, 'z': -0.016691158}, {'x': 0.53960544, 'y': 0.19867118, 'z': -0.022496894}, {'x': 0.5200173, 'y': 0.24284497, 'z': -0.029544042}, {'x': 0.60045314, 'y': 0.1998046, 'z': -0.040305816}, {'x': 0.5561593, 'y': 0.24724272, 'z': -0.055317394}, {'x': 0.5310527, 'y': 0.2762247, 'z': -0.061918586}, {'x': 0.51013184, 'y': 0.2974146, 'z': -0.06583886}, {'x': 0.6218219, 'y': 0.24165823, 'z': -0.042312164}, {'x': 0.57844573, 'y': 0.29860744, 'z': -0.057358146}, {'x': 0.5465466, 'y': 0.3352823, 'z': -0.06409986}, {'x': 0.52153265, 'y': 0.3592567, 'z': -0.07026574}, {'x': 0.63791025, 'y': 0.2769149, 'z': -0.042803846}, {'x': 0.6006995, 'y': 0.33498996, 'z': -0.054603003}, {'x': 0.5707777, 'y': 0.36874065, 'z': -0.05960848}, {'x': 0.54510313, 'y': 0.3890803, 'z': -0.064214505}, {'x': 0.6496781, 'y': 0.30460906, 'z': -0.043253858}, {'x': 0.625367, 'y': 0.36255825, 'z': -0.054052617}, {'x': 0.6050887, 'y': 0.39506626, 'z': -0.059133682}, {'x': 0.58624977, 'y': 0.41754797, 'z': -0.06308594}]}

file = "augmentedImgs/rotatedImg-45/001-rotatedImg-45.jpg"

flipped_points = flip_points_horizontally(handLandMark)

file = "random_images/001.jpg"

image = Image.open(file)
draw = ImageDraw.Draw(image)
print(image)
size = 5
center_x, center_y = width/2, height/2
center_x, center_y = 0.5, 0.5
for point in flipped_points['landmark']:

    xMain = point['x']# * width
    yMain = point['y']# * height

    xRotatedNew, yRotatedNew = rotate_point_new(xMain, yMain, 45, center_x, center_y)


    xRotatedNew*=width
    yRotatedNew*=height

    draw.ellipse((xRotatedNew-size, yRotatedNew-size, xRotatedNew+size, yRotatedNew+size), fill=(0, 0, 0), outline="red")

    
image.save("output2.png")




"""
#file = "random_images/001.jpg"
print(file)
im = Image.open(file)
im = im.transpose(Image.FLIP_LEFT_RIGHT)
# Create an ImageDraw object
draw = ImageDraw.Draw(im)
# Iterate through the handLandMark dictionary
order = [4,3,2,1,0,8,7,6,5,0,12,11,10,9,0,16,15,14,13,0,20,19,18,17,0]
# Iterate through the handLandMark dictionary
for i, index in enumerate(order):
    point = handLandMark['landmark'][index]
    # Extract the x and y coordinates
    x = point['x']
    y = point['y']
    # scale the coordinates
    x_scaled = int(x*width)
    y_scaled = int(y*height)

    # Draw the point on the image
    draw.point((x_scaled, y_scaled), fill=(255, 0, 255))

    # Draw a connector to the next point
    if i < len(order)-1:
        next_index = order[i+1]
        next_point = handLandMark['landmark'][next_index]
        next_x = next_point['x']
        next_y = next_point['y']
        next_x_scaled = int(next_x*width)
        next_y_scaled = int(next_y*height)
        draw.line((x_scaled, y_scaled, next_x_scaled, next_y_scaled), fill=(255, 0, 0))


# Save the modified image
im.save("flippedImagePointDrawn.jpg")
"""