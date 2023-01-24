from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import textwrap, os
import os
import numpy as np
from pprint import pprint
import textwrap

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

def makeTextImage(text, width):
    defaultImage = Image.new("RGB", (1920, 1080), (0, 0, 0))
    draw = ImageDraw.Draw(defaultImage)
    font = ImageFont.truetype("arial.ttf", 80)
    wrapped_text = textwrap.fill(text, width)
    text_w, text_h = draw.textsize(wrapped_text, font=font)
    draw.text(((1920 - text_w) / 2, (1080 - text_h) / 2), wrapped_text, (255, 255, 255), font=font)
    return defaultImage
def makeFolder(folderName):
    """
    Created directory if not already made
    """
    if not os.path.exists(folderName):
        os.mkdir(folderName)

choosenPhotos = ["006", "009", "018", "043", "045"]
choosenPhotos = ["047", "049", "051", "052", "061"]
choosenPhotos = ["065", "073", "078", "080", "088"]

photosPaths = []

folderAugmentedImgs = "augmentedImgsMediaPipe"
makeFolder("GIF-Images")
for imgNum in choosenPhotos:
    gif_images = []
    for augment in os.listdir(folderAugmentedImgs):
        im = Image.open(folderAugmentedImgs + "/" + augment + "/" + imgNum + "-" + augment.replace("-mediaPipe","") + ".jpg", 'r')
        photosPaths.append(im)
        gif_images.append(im)
    # Create the GIF
    gif_images[0].save("GIF-Images/" + imgNum + '.gif', save_all=True, append_images=gif_images[1:])




x,y = photosPaths[0].size
ncol = 5
nrow = 13
gridImages = Image.new('RGB',(x * ncol, y * nrow))
for i in range(len(photosPaths)):
    px, py = x * int(i/nrow), y * (i % nrow)
    #px, py = x * (i % ncol), y * int(i/ncol)
    gridImages.paste(photosPaths[i], (px, py))

title = "Combined Images for: " + ", ".join(map(str,choosenPhotos))
titleImage = makeTextImage(title, 100)
title_w, title_h = titleImage.size
gridImages = Image.new('RGB',(x * ncol, (y * nrow) + title_h + 100)) # added an extra 100 pixels to the height
gridImages.paste(titleImage, (0,0))
for i in range(len(photosPaths)):
    px, py = x * int(i/nrow), y * (i % nrow) + title_h + 100
    gridImages.paste(photosPaths[i], (px, py))

width, height = gridImages.size
max_dim = 100000
if width > height:
    new_width = max_dim
    new_height = int(new_width * height / width)
else:
    new_height = max_dim
    new_width = int(new_height * width / height)
gridImages = gridImages.resize((new_width, new_height))

# JPG better storage than PNG
gridImages.save("allGridImages" + ",".join(map(str,choosenPhotos)) + ".jpg")

# gridImagesSized = gridImages.resize((int(gridImages.size[0]/2), int(gridImages.size[1]/2)), Image.ANTIALIAS)
# gridImagesSized.save("allGridImagesStorage.png", optimize=True)
