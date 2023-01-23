import pickle
import numpy as np
from pprint import pprint
# load the array from the binary file
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)


def detect_outliers(data):
    # Initialize an empty dictionary to store outliers
    outliers = {}
    # Loop through each image in the data
    for image in data:
        # Get the image name and landmarks
        image_name = image[0]
        landmarks = image[1]['landmark']
        # Calculate the mean and standard deviation of the x and y coordinates
        x_coords = [l['x'] for l in landmarks]
        y_coords = [l['y'] for l in landmarks]
        x_mean, y_mean = np.mean(x_coords), np.mean(y_coords)
        x_std, y_std = np.std(x_coords), np.std(y_coords)
        # Loop through each landmark
        for i, landmark in enumerate(landmarks):
            # Check if the x or y value is more than 2 standard deviations away from the mean
            if abs(landmark['x'] - x_mean) > 2 * x_std or abs(landmark['y'] - y_mean) > 2 * y_std:
                # Add the outlier to the dictionary
                if image_name not in outliers:
                    outliers[image_name] = []
                #outliers[image_name].append((i, landmark['x'], landmark['y'],image_name))
                outliers[image_name].append((i+1, landmark['x'], landmark['y'],image_name))
    # Loop through the outliers dictionary and print the outliers in the desired format
    for img, outliers in outliers.items():
        for outlier in outliers:
            #print("Outlier detected for point {} in file {} with value 'x': {}, 'y': {}".format(outlier[0]+1, outlier[3], outlier[1], outlier[2]))
            print("Outlier detected for point {} in file {} with value 'x': {}, 'y': {}".format(outlier[0], outlier[3], outlier[1], outlier[2]))


ct = 1
for eachFile in data:
    print("-"*20 + str(ct) + "-"*20)
    detect_outliers(eachFile)
    ct+=1