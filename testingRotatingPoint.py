from utils import *
import os
import pickle




#changePoint(augmentType, xP, yP)


"""
------------------
{'x': 0.5351898, 'y': 0.24521858, 'z': -0.053861715}
{'x': 0.5351898, 'y': 0.24521858, 'z': -0.053861715}
------------------
{'x': 0.53442585, 'y': 0.29258516, 'z': -0.060371716}
{'x': 0.53442585, 'y': 0.29258516, 'z': -0.060371716}
------------------
{'x': 0.5297064, 'y': 0.33082727, 'z': -0.06558263}
{'x': 0.5297064, 'y': 0.33082727, 'z': -0.06558263}



"""

import math


def rotate_point_normlized(x, y, width = 1920, height=1080):
    radians = math.radians(45)  # convert degrees to radians
    new_x = (x - 0.5) * math.cos(radians) - (y - 0.5) * math.sin(radians) + 0.5
    new_y = (x - 0.5) * math.sin(radians) + (y - 0.5) * math.cos(radians) + 0.5
    return new_x * width, new_y * height, new_x, new_y

x = 0.67807657
y = 0.20800887
width = 1920
height = 1080
rotated_x, rotated_y, new_x, new_y = rotate_point_normlized(x, y)
print("Scaled to image size point: ",rotated_x, rotated_y)

print("Scaled to [0,1] point: ",x, y)
print("Scaled to [0,1] point: ",new_x, new_y)
