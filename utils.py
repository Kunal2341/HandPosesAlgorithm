import os 
import numpy as np
import math

def makeFolder(folderName):
    """
    Created directory if not already made
    """
    if not os.path.exists(folderName):
        os.mkdir(folderName)

def rotate_around_point_lowperf(point, radians, origin):
    """
    Rotate a point around a given point, doesn't work for normalized points
    """
    x, y = point
    ox, oy = origin

    qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
    qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)

    return int(qx), int(qy)

def rotate_point_normlized(x, y, rotation, width = 1920, height=1080):
    """
    Rotate a normalized point around center, (0.5,0.5)
    """
    radians = math.radians(rotation)  # convert degrees to radians
    new_x = (x - 0.5) * math.cos(radians) - (y - 0.5) * math.sin(radians) + 0.5
    new_y = (x - 0.5) * math.sin(radians) + (y - 0.5) * math.cos(radians) + 0.5
    #return new_x * width, new_y * height, new_x, new_y
    return new_x, new_y
def changePoint(augmentType, xP, yP, origin=(1920/2, 1080/2), normalized=False):
    """
    Different changes to points depending on types of augmented image
    """
    if not normalized:
        if augmentType == "flippedImg":
            return xP, 1080-yP-1
        elif augmentType == "rotatedImg-45":
            return rotate_around_point_lowperf((xP, yP), 45, origin)
        elif augmentType == "rotatedImg-90":
            return rotate_around_point_lowperf((xP, yP), 90, origin)
        else:
            return xP, yP
    else:
        if augmentType == "rotatedImg-45":
            xFlippedPoint, yFlippedPoint = flip_points_horizontally(xP, yP)
            return rotate_point_new(xFlippedPoint, yFlippedPoint, 45, 0.5, 0.5)
        elif augmentType == "rotatedImg-90":
            xFlippedPoint, yFlippedPoint = flip_points_horizontally(xP, yP)
            return rotate_point_new(xFlippedPoint, yFlippedPoint, 90, 0.5, 0.5)
            #return rotate_point_normlized(xP, yP, 90)
        elif augmentType == "flippedImg":
            return xP, 1 - yP


def z_score_outliers(data, threshold=3):
    """
    Calculate the outliers for the x,y valeues
    """
    # Separate the x and y values into separate arrays
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    # Combine the x and y values into one array
    data = np.column_stack((x, y))
    # Compute the Z-scores for each point
    z_scores = np.abs(stats.zscore(data))
    # Identify the points that have Z-scores above the threshold
    outliers = np.where(z_scores > threshold)
    return outliers

def flip_points_horizontally(x, y):
    return 1 - x, y

def rotate_point_new(x, y, angle, center_x, center_y):
    angle = math.radians(angle)
    x_temp = x - center_x
    y_temp = y - center_y
    new_x = x_temp * math.cos(angle) - y_temp * math.sin(angle) + center_x
    new_y = x_temp * math.sin(angle) + y_temp * math.cos(angle) + center_y
    return new_x, new_y
