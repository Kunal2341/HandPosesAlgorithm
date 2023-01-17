from PIL import Image
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


choosenPhotos = ["001", "025", "082", "062", "017"]
photosPaths = []
#13
for imgNum in choosenPhotos:
    for augment in os.listdir("augmentedImgs"):
        im = Image.open("augmentedImgs/"+ augment + "/" + imgNum + "-" + augment + ".jpg", 'r')
        photosPaths.append(im)
"""for imgNum in choosenPhotos:
    imgStyles = []
    for augment in os.listdir("augmentedImgs"):
        imgStyles.append("augmentedImgs/" + imgNum + "-" + augment)
    photosPaths.append(imgStyles)

print(photosPaths[0])"""
#image_grid(photosPaths, 5, 13)

def display_images(
    images, 
    columns=5, width=20, height=8, max_images=15, 
    label_wrap_length=50, label_font_size=8):

    if not images:
        print("No images to display.")
        return 

    if len(images) > max_images:
        print(f"Showing {max_images} images of {len(images)}:")
        images=images[0:max_images]

    height = max(height, int(len(images)/columns) * height)
    plt.figure(figsize=(width, height))
    for i, image in enumerate(images):

        plt.subplot(int(len(images) / columns + 1), columns, i + 1)
        plt.imshow(image)

        if hasattr(image, 'filename'):
            title=image.filename
            if title.endswith("/"): title = title[0:-1]
            title=os.path.basename(title)
            title=textwrap.wrap(title, label_wrap_length)
            title="\n".join(title)
            plt.title(title, fontsize=label_font_size); 
#display_images(photosPaths)

x,y = photosPaths[0].size
ncol = 5
nrow = 13
cvs = Image.new('RGB',(x*ncol,y*nrow))
for i in range(len(photosPaths)):
    px, py = x*(i%ncol), y*int(i/ncol)
    cvs.paste(photosPaths[i],(px,py))
cvs.save("tets.png")