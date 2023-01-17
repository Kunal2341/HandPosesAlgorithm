import cv2
import mediapipe as mp
import os 
import numpy as np
from pprint import pprint
import math


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def makeFolder(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

makeFolder("augmentedImgsMediaPipe")
for augment in os.listdir("augmentedImgs"):
    makeFolder("augmentedImgsMediaPipe/" + augment + "-mediaPipe")

allImagesPathGrouped = []
for imgNumber in range(100):
    eachImgAugments = []
    for augment in sorted(os.listdir("augmentedImgs")):
        eachImgAugments.append("augmentedImgs/" + augment + "/" + sorted(os.listdir("augmentedImgs/" + augment))[imgNumber])
    allImagesPathGrouped.append(eachImgAugments)

#pprint(allImagesPathGrouped[10])

#IMAGE_FILES = []
#for img in os.listdir(folderName):
#    IMAGE_FILES.append(folderName + "/" + img)

#resultesFolder = "random_images_results_final/"
#makeFolder(resultesFolder)

#1920, 1080

def rotate_around_point_lowperf(point, radians, origin=(1920/2, 1080/2)):
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

def changePoint(augmentType, xP, yP):
    if augmentType == "flippedImg":
        return xP, 1080-yP-1
    elif augmentType == "rotatedImg-45":
        return rotate_around_point_lowperf((xP, yP), 45)
    elif augmentType == "rotatedImg-90":
        return rotate_around_point_lowperf((xP, yP), 90)
    else:
        return xP, yP

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 3

resultsArray = []

for imgGroup in allImagesPathGrouped:
    print("-"*20)
    print("Running " + imgGroup[0])
    tipFingerNumbers = {}
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(imgGroup):

            resultingPath = "augmentedImgsMediaPipe/" + os.path.split(os.path.dirname(file))[1] + "-mediaPipe/" + os.path.split(file)[1]

            detailsArray = []
            # Read an image, flip it around y-axis for correct handedness output (see
            # above).
            image = cv2.flip(cv2.imread(file), 1)
            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # Print handedness and draw hand landmarks on the image.
            # print('Handedness:', results.multi_handedness)
            if not results.multi_hand_landmarks:
                #print(file)
                cv2.imwrite(resultingPath, cv2.imread(file))
                continue
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                #print('hand_landmarks:', hand_landmarks)
                #print(
                #    f'Index finger tip coordinates: (',
                #    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                #    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
                #)
                mp_drawing.draw_landmarks(
                    annotated_image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                #for hand_landmarks in results.multi_hand_landmarks:
                xTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                yTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
            
            xTipP, yTipP = changePoint(os.path.split(os.path.dirname(file))[1], xTxt, yTxt)
            
            tipFingerNumbers.update({os.path.split(os.path.dirname(file))[1] : (xTipP, yTipP)})
            
            newxTxt = annotated_image.shape[1] - xTxt - 1
            newyTxt = yTxt - 10
            annotated_image = cv2.flip(annotated_image, 1)

            cv2.putText(annotated_image, "(" + str(newxTxt) + "," + str(yTxt) +  ")", (newxTxt, newyTxt), 
                        font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.putText(annotated_image, str(file[-6:]), (0,40), font, fontScale, color, thickness, cv2.LINE_AA)
            
            
            
            
            
            cv2.imwrite(resultingPath, annotated_image)

            # For display to user
            # windowName = "Image" + str(file)
            # percentSmall = 0.55
            # size = ((int) (annotated_image.shape[1]*percentSmall), (int) (annotated_image.shape[0]*percentSmall))
            # annotated_image = cv2.resize(annotated_image, size)
            
            #print("")
            #print("\t" + file[-6:])
            #print("\tSize--- " + str(annotated_image.shape[0]) + ", " + str(annotated_image.shape[1]))
            #print("\tFinger--- "+ str(newxTxt) + ", " + str(yTxt))
            #print("-"*20)

            #cv2.imshow(windowName, annotated_image)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

    print(tipFingerNumbers)


#[(819, 368), (820, 369), (820, 366), (819, 375), (818, 372), (818, 366), (818, 365), (820, 707), (819, 368), (979, 321), (1131, 402)]
#[(819, 368), (820, 369), (820, 366), (819, 375), (818, 372), (818, 366), (818, 365), (820, 372), (819, 368), (1156, 441), (1006, 754)]
