import os 
import numpy as np
import math

def makeFolder(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

def rotate_around_point_lowperf(point, radians, origin):
    """Rotate a point around a given point.
    
    I call this the "low performance" version since it's recalculating
    the same values more than once [cos(radians), sin(radians), x-ox, y-oy).
    It's more readable than the next function, though.
    """
    x, y = point
    ox, oy = origin

    qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
    qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)

    return int(qx), int(qy)

def changePoint(augmentType, xP, yP, origin=(1920/2, 1080/2)):
    if augmentType == "flippedImg":
        return xP, 1080-yP-1
    elif augmentType == "rotatedImg-45":
        return rotate_around_point_lowperf((xP, yP), 45, origin)
    elif augmentType == "rotatedImg-90":
        return rotate_around_point_lowperf((xP, yP), 90, origin)
    else:
        return xP, yP

def z_score_outliers(data, threshold=3):
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