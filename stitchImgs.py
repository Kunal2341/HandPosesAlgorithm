from PIL import Image
import os
mediapipe = "mediapipe-results-all/"
mmpose = "mmpose-results-images-all/"
orginal = "random_images/"

numMediaPipeImgs = len([name for name in os.listdir(mediapipe)])
numMMposeImgs = len([name for name in os.listdir(mmpose)])
numOriginal = len([name for name in os.listdir(orginal)])

print("Number of Media pipe images - {}\nNumber of MMpose images - \
        {}\nNumber of orginal images - {}".format(
            numMediaPipeImgs, numMMposeImgs, numOriginal))

if numMediaPipeImgs != numMMposeImgs:
    raise Exception("Not same number of images")

for img in os.listdir(orginal):
    #print(img)
    tempMMposeName = ""
    if img[0] == "0" and img[1] == "0":
        tempMMposeName = "vis_00" + img[2] + ".jpg"
    else:
        tempMMposeName = "vis_0" + img[1:3] + ".jpg"
    tempMediaPipeName = ""
    if img[0] == "0" and img[1] == "0":
        tempMediaPipeName = img[2:]
    else:
        tempMediaPipeName = img[1:]
    if not os.path.exists(mediapipe + tempMediaPipeName):
        if os.path.exists(mediapipe + tempMediaPipeName[:-4] + ".png"):
            tempMediaPipeName = tempMediaPipeName[:-4] + ".png"
        else:
            print("idk")
    
    img1 = Image.open(mediapipe + tempMediaPipeName)
    img2 = Image.open(mmpose + tempMMposeName)
    img3 = Image.open(orginal + img)

    (w1, h1) = img1.size
    (w2, h2) = img2.size
    
    resultWidth = w1 + w2
    resultHeight = max(h1,h2)
    result = Image.new('RGB', (resultWidth, resultHeight))
    result.paste(im=img1, box=(0,0))
    result.paste(im=img2, box=(w1,0))

    result.save("combinedResults/" + img[:-4] + "-combined.jpg")

