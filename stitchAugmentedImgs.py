from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import textwrap, os
import os
import numpy as np

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

def makeTextImage(text):
    defaultImage = Image.new("RGB", (1920, 1080), (0, 0, 0))
    draw = ImageDraw.Draw(defaultImage)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 200)
    draw.text((1920/2, 1080/2 - (len(text) * 10)), text, (255, 255, 255), font=font)
    return defaultImage
choosenPhotos = ["001", "025", "082", "062", "017"]
photosPaths = []
#Add the 0 image

photosPaths.append(makeTextImage("RANDOM IMAGES ON GOOGLE MEDIA PIPE"))
for imgNumText in choosenPhotos:
    photosPaths.append(makeTextImage("Image " + imgNumText))
for imgNum in choosenPhotos:
    for augment in os.listdir("augmentedImgs"):
        im = Image.open("augmentedImgs/"+ augment + "/" + imgNum + "-" + augment + ".jpg", 'r')
        photosPaths.append(im)

x,y = photosPaths[0].size
ncol = 6
nrow = 14
gridImages = Image.new('RGB',(x * ncol, y * nrow))
for i in range(len(photosPaths)):
    px, py = x * (i % ncol), y * int(i/ncol)
    gridImages.paste(photosPaths[i], (px, py))
gridImages.save("allGridImages.png")