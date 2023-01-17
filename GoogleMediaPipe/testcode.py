#import cv2
#import mediapipe as mp
import os 
#import numpy as np

#mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles
#mp_hands = mp.solutions.hands


def makeFolder(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

makeFolder("augmentedImgsMediaPipe")
for augment in os.listdir("augmentedImgs"):
    makeFolder(augment + "-mediaPipe")


#folderName = os.path.join(os.path.dirname(os.getcwd()), "random_images")
#print(os.path.exists(folderName))
#print(folderName)

allImagesPathGrouped = []
for imgNumber in range(100):
    eachImgAugments = []
    for augment in os.listdir("augmentedImgs"):
        eachImgAugments.append("augmentedImgs/" + augment + "/" + os.listdir("augmentedImgs/" + augment)[imgNumber])
    allImagesPathGrouped.append(eachImgAugments)


print(allImagesPathGrouped[0])