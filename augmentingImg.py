from PIL import Image, ImageEnhance, ImageOps, ImageFont, ImageDraw
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
mainFolderName = "augmentedImgs"
if not os.path.exists(os.path.join(os.getcwd(), mainFolderName)):
    os.mkdir(mainFolderName)
"""
def makeFolder(folderName):
    originalPath = os.path.join(os.getcwd() + "augmentedImgs")
    if not os.path.exists(os.path.join(originalPath, folderName)):
        os.mkdir(os.path.join(originalPath, folderName))
"""

def makeFolder(folderName):
    if not os.path.exists("augmentedImgs\\" + folderName):
        os.mkdir("augmentedImgs\\" + folderName)

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

brightFolder125 = "brightenedImg-1.25"
brightFolder150 = "brightenedImg-1.50"
brightFolder175 = "brightenedImg-1.75"
darkenFolder125 = "darkenImg-0.75"
darkenFolder150 = "darkenImg-0.50"
darkenFolder175 = "darkenImg-0.25"
flippedFolder = "flippedImg"
contrast100 = "contrastImg-100"
contrast200 = "contrastImg-200"
resolution50 = "resolution-50"
rotatedImg45 = "rotatedImg-45"
rotatedImg90 = "rotatedImg-90"
grayscaled = "grayScaledImg"

makeFolder(brightFolder125)
makeFolder(brightFolder150)
makeFolder(brightFolder175)
makeFolder(darkenFolder125)
makeFolder(darkenFolder150)
makeFolder(darkenFolder175)
makeFolder(flippedFolder)
makeFolder(contrast100)
makeFolder(contrast200)
makeFolder(resolution50)
makeFolder(rotatedImg45)
makeFolder(rotatedImg90)
makeFolder(grayscaled)

def writeTextChange(image, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 75)
    #font = ImageFont.load_default(size=24)
    draw.text((10, 10), text, (255,255,255),font=font)
    return image

for img in os.listdir(orginal):
    im = Image.open(orginal + img)
    enhancer = ImageEnhance.Brightness(im)
    im_output125 = enhancer.enhance(1.25)
    im_output150 = enhancer.enhance(1.5)
    im_output175 = enhancer.enhance(1.75)
    writeTextChange(im_output125, img[:-4] + " - Brighten by 25%")
    writeTextChange(im_output150, img[:-4] + " - Brighten by 50%")
    writeTextChange(im_output175, img[:-4] + " - Brighten by 75%")
    im_output125.save(mainFolderName + "/" + brightFolder125 + "/" + img[:-4] + "-" + brightFolder125 + ".jpg")
    im_output150.save(mainFolderName + "/" + brightFolder150 + "/" + img[:-4] + "-" + brightFolder150 + ".jpg")
    im_output175.save(mainFolderName + "/" + brightFolder175 + "/" + img[:-4] + "-" + brightFolder175 + ".jpg")
    im_darken125 = enhancer.enhance(0.75)
    im_darken150 = enhancer.enhance(0.50)
    im_darken175 = enhancer.enhance(0.25)
    writeTextChange(im_darken125, img[:-4] + " - Darken by 25%")
    writeTextChange(im_darken150, img[:-4] + " - Darken by 50%")
    writeTextChange(im_darken175, img[:-4] + " - Darken by 75%")
    im_darken125.save(mainFolderName + "/" + darkenFolder125 + "/" + img[:-4] + "-" + darkenFolder125 + ".jpg")
    im_darken150.save(mainFolderName + "/" + darkenFolder150 + "/" + img[:-4] + "-" + darkenFolder150 + ".jpg")
    im_darken175.save(mainFolderName + "/" + darkenFolder175 + "/" + img[:-4] + "-" + darkenFolder175 + ".jpg")
    im_flipped = ImageOps.flip(im)
    writeTextChange(im_flipped, img[:-4] + " - Flipped Image")
    im_flipped.save(mainFolderName + "/" + flippedFolder + "/" + img[:-4] + "-" + flippedFolder + ".jpg")
    im_contrast100 = change_contrast(im, 100)
    im_contrast200 = change_contrast(im, 200)
    writeTextChange(im_contrast100, img[:-4] + " - Changed Contrast 100")
    writeTextChange(im_contrast200, img[:-4] + " - Changed Contrast 200")
    im_contrast100.save(mainFolderName + "/" + contrast100 + "/" + img[:-4] + "-" + contrast100 + ".jpg")
    im_contrast200.save(mainFolderName + "/" + contrast200 + "/" + img[:-4] + "-" + contrast200 + ".jpg")
    im_resolution = im
    writeTextChange(im_resolution, img[:-4] + " - Resolution by 50%")
    im_resolution.save(mainFolderName + "/" + resolution50 + "/" + img[:-4] + "-" + resolution50 + ".jpg", quality=50)
    im_rotate45 = im.rotate(45)
    im_rotate90 = im.rotate(90)
    writeTextChange(im_rotate45, img[:-4] + " - Rotate by 45*")
    writeTextChange(im_rotate90, img[:-4] + " - Rotate by 90*")
    im_rotate45.save(mainFolderName + "/" + rotatedImg45 + "/" + img[:-4] + "-" + rotatedImg45 + ".jpg")
    im_rotate90.save(mainFolderName + "/" + rotatedImg90 + "/" + img[:-4] + "-" + rotatedImg90 + ".jpg")
    im_grayscale = im.convert('L')
    im_grayscale.save(mainFolderName + "/" + grayscaled + "/" + img[:-4] + "-" + grayscaled + ".jpg")