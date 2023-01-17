from PIL import Image, ImageEnhance
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

def makeFolder(folderName):
    if not os.path.exists(os.path.join(os.getcwd(), folderName)):
        os.mkdir(folderName)

#Brightened the image by 25 Percent, 50 Percent, and 75 Percent


brightFolder125 = "brightenedImg-1.25"
brightFolder150 = "brightenedImg-1.50"
brightFolder175 = "brightenedImg-1.75"
darkenFolder125 = "darkenImg-0.75"
darkenFolder150 = "darkenImg-0.50"
darkenFolder175 = "darkenImg-0.25"

makeFolder(brightFolder125)
makeFolder(brightFolder150)
makeFolder(brightFolder175)
makeFolder(darkenFolder125)
makeFolder(darkenFolder150)
makeFolder(darkenFolder175)



for img in os.listdir(orginal):
    im = Image.open(orginal + img)
    enhancer = ImageEnhance.Brightness(im)
    im_output125 = enhancer.enhance(1.25)
    im_output150 = enhancer.enhance(1.5)
    im_output175 = enhancer.enhance(1.75)
    im_output125.save(brightFolder125 + "/" + img[:-4] + "-125Bright.jpg")
    im_output150.save(brightFolder150 + "/" + img[:-4] + "-150Bright.jpg")
    im_output175.save(brightFolder175 + "/" + img[:-4] + "-175Bright.jpg")
    im_darken125 = enhancer.enhance(0.75)
    im_darken150 = enhancer.enhance(0.50)
    im_darken175 = enhancer.enhance(0.25)
    im_darken125.save(darkenFolder125 + "/" + img[:-4] + "-125Dark.jpg")
    im_darken150.save(darkenFolder150 + "/" + img[:-4] + "-150Dark.jpg")
    im_darken175.save(darkenFolder175 + "/" + img[:-4] + "-175Dark.jpg")
    
