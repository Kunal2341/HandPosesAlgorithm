from PIL import Image
import os
#mediapipe = "mediapipe-results-all/"
#mmpose = "mmpose-results-images-all/"
orginal = "random_images/"

#numMediaPipeImgs = len([name for name in os.listdir(mediapipe)])
#numMMposeImgs = len([name for name in os.listdir(mmpose)])
numOriginal = len([name for name in os.listdir(orginal)])

#print("Number of Media pipe images - {}\nNumber of MMpose images - \
#        {}\nNumber of orginal images - {}".format(
#            numMediaPipeImgs, numMMposeImgs, numOriginal))

if not os.path.exists(os.path.join(os.getcwd(), "convertedImgs")):
    os.mkdir("convertedImgs")


for img in os.listdir(orginal):
    print(img)