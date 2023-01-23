from utils import *
import cv2
import mediapipe as mp
import os 
import numpy as np
from pprint import pprint
import math
import pickle
from google.protobuf import text_format
from google.protobuf.json_format import MessageToDict

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

makeFolder("augmentedImgsMediaPipe")
for augment in os.listdir("augmentedImgs"):
    makeFolder("augmentedImgsMediaPipe/" + augment + "-mediaPipe")

allImagesPathGrouped = []
for imgNumber in range(100):
    eachImgAugments = []
    for augment in sorted(os.listdir("augmentedImgs")):
        eachImgAugments.append("augmentedImgs/" + augment + "/" + sorted(os.listdir("augmentedImgs/" + augment))[imgNumber])
    allImagesPathGrouped.append(eachImgAugments)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 3

resultsArray = []

makeFolder("allEditsStitched")
l = 0
for imgGroup in allImagesPathGrouped:
    count = 1
    cleanImgPath = os.path.split(imgGroup[0])[1][0:3] + ".jpg"
    imgEditsAll = cv2.flip(cv2.imread("random_images/" + cleanImgPath), 1)

    print("-"*40)
    print("Running " + imgGroup[0])
    tipFingerNumbers = {}
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(imgGroup):
            augmentType = os.path.split(os.path.dirname(file))[1]
            resultingPath = "augmentedImgsMediaPipe/" + augmentType + "-mediaPipe/" + os.path.split(file)[1]
            detailsArray = []
            image = cv2.flip(cv2.imread(file), 1)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # Print handedness and draw hand landmarks on the image.
            # print('Handedness:', results.multi_handedness)
            if not results.multi_hand_landmarks:
                print(f"\t{count} - Failed in {augmentType}")
                cv2.imwrite(resultingPath, cv2.imread(file))
                count+=1
                continue
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                if augmentType == "rotatedImg-45" or augmentType == "rotatedImg-90" or augmentType == "flippedImg":
                    dictLandmark = MessageToDict(hand_landmarks)
                    
                    print("\tChanged------------" + augmentType + "-------")
                    
                    print(len(dictLandmark['landmark']))
                    print(len(hand_landmarks.landmark))


                    print(dictLandmark['landmark'])
                    print(hand_landmarks.landmark)
                    print("-"*20)

                    countLandMark = 0
                    for point in dictLandmark['landmark']:
                        
                        hand_landmarks.landmark[countLandMark].x, hand_landmarks.landmark[countLandMark].y = changePoint(augmentType, point['x'], point['y'], normalized=True)
                        print(hand_landmarks.landmark[countLandMark].x, hand_landmarks.landmark[countLandMark].y)

                        countLandMark+=1
                    
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

                mp_drawing.draw_landmarks(
                    imgEditsAll,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                count+=1
                print(f"\t{count} - Got it for {augmentType}")

                #for hand_landmarks in results.multi_hand_landmarks:
                xTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                yTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
            xTipP, yTipP = changePoint(augmentType, xTxt, yTxt)
            
            tipFingerNumbers.update({augmentType : (xTipP, yTipP)})
            
            newxTxt = annotated_image.shape[1] - xTxt - 1
            newyTxt = yTxt - 10
            annotated_image = cv2.flip(annotated_image, 1)

            cv2.putText(annotated_image, "(" + str(newxTxt) + "," + str(yTxt) +  ")", (newxTxt, newyTxt), 
                        font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.putText(annotated_image, str(file[-6:]), (0,40), font, fontScale, color, thickness, cv2.LINE_AA)
            
            cv2.putText(imgEditsAll, augmentType, (xTipP, yTipP), font, fontScale, color, thickness, cv2.LINE_AA)
            
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

    cv2.imwrite("allEditsStitched/" + os.path.split(imgGroup[0])[1][0:3] + "-ALL.jpg", imgEditsAll)
    print("The file changed!")
    #pprint(tipFingerNumbers)
    resultsArray.append(tipFingerNumbers)
    print(f"{count} Different drawings on the image")
    
    if l == 2:
        break
    l += 1

with open("tipFingerPoint.pkl", "wb") as f:
    f.dump(resultsArray)
