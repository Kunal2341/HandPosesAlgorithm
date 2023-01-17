import cv2
import mediapipe as mp
import os 
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


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



#IMAGE_FILES = []
#for img in os.listdir(folderName):
#    IMAGE_FILES.append(folderName + "/" + img)



#resultesFolder = "random_images_results_final/"
#makeFolder(resultesFolder)


font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 3


resultsArray = []

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    for idx, file in enumerate(IMAGE_FILES):
        
        detailsArray = []

        # Read an image, flip it around y-axis for correct handedness output (see
        # above).
        image = cv2.flip(cv2.imread(file), 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Print handedness and draw hand landmarks on the image.
        # print('Handedness:', results.multi_handedness)
        if not results.multi_hand_landmarks:
            continue
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            """
            print('hand_landmarks:', hand_landmarks)
            print(
                f'Index finger tip coordinates: (',
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
            )
            """
            mp_drawing.draw_landmarks(
                annotated_image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            xTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
            yTxt = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
        newxTxt = annotated_image.shape[1] - xTxt - 1
        newyTxt = yTxt - 10
        annotated_image = cv2.flip(annotated_image, 1)

        cv2.putText(annotated_image, "(" + str(newxTxt) + "," + str(yTxt) +  ")", (newxTxt, newyTxt), font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.putText(annotated_image, str(file[-6:]), (0,40), font, fontScale, color, thickness, cv2.LINE_AA)
        
        cv2.imwrite(resultesFolder + str(idx) + '.png', annotated_image)



        # For display to user
        windowName = "Image" + str(file)
        percentSmall = 0.55
        size = ((int) (annotated_image.shape[1]*percentSmall), (int) (annotated_image.shape[0]*percentSmall))
        annotated_image = cv2.resize(annotated_image, size)
        print("")
        print("\t" + file[-6:])
        print("\tSize--- " + str(annotated_image.shape[0]) + ", " + str(annotated_image.shape[1]))
        print("\tFinger--- "+ str(newxTxt) + ", " + str(yTxt))
        print("-"*20)

        #cv2.imshow(windowName, annotated_image)
        
        


        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

