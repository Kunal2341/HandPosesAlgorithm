# HandPosesAlgorithm
# Augmenting images

~~**Problem** --> Failing to properly stack the images becuase of the rotation and normalizing of the points in Google Media Pipes Pipeline.~~

## Grid of images 

Below is the grid of images with each on labeled on the following images
|Grid Images|Stacked Images for `043`|GIF for `043`
|-|-|-|
|![Grid of augmented images](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allGridImages006,009,018,043,045.jpg?raw=true)|![stackedImages Example](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/043-ALL.jpg?raw=true)|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/043.gif?raw=truef" alt="GIF of 043 image" loop=inf/>|

## Analysis 


|Bad Image|Problem|GIF Image|Helper Augments|
|-|-|-|-|
|![stacked 006 image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/006-ALL.jpg?raw=true)|Thumb prediction because of hidden also (*Middle Finger stuggles with exact tip point due to covered hand*)|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/006.gif?raw=truef" alt="GIF of 006 image" loop=inf/>|`darken 75%` & `grayscale`|
![stacked 009 image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/009-ALL.jpg?raw=true)|Middle, Ring, and Pinky finger points prediction due to covered view|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/006.gif?raw=truef" alt="GIF of 009 image" loop=inf/>|`resolution 50%`|
![stacked 018 image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/018-ALL.jpg?raw=true)|Main pointer fail to reach correct tip|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/018.gif?raw=truef" alt="GIF of 018 image" loop=inf/>|`darken 50%` & `grayscale` & `brighten 75%`|
![stacked 043 image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/043-ALL.jpg?raw=true)|Nothing too bad good average on detected images|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/043.gif?raw=truef" alt="GIF of 043 image" loop=inf/>|n/a|
![stacked 045 image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/allEditsStitched/045-ALL.jpg?raw=true)|Middle and ring finger predictions wrong, covered and curled|<img src="https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/043.gif?raw=truef" alt="GIF of 043 image" loop=inf/>|none|



## Running the code
Use `conda activate HandPose`

Check out image `vis_006` for possible mistakes in google media pipe

Change the image using the following adjustments only with **google media pipe**

- [x] Brighten the image
- [x] Darken the image
- [x] Flip the image horizontally
- [x] Increase/decrease the image contrast
- [x] Lower the resolution by 50% 
- [x] Rotate the image by 45 degrees
- [x] Rotate the image by 90 degrees
- [x] Convert the image to grayscale

Test out results by draw each image on top of each other 

Using the x,y points take the average of the outputs and remove outliers

# Different Model Tests
Running different tests on a sample of a 100 hand images to see which model works the best for our use case.

|Model|Description|Image Example &nbsp &nbsp &nbsp &nbsp &nbsp|
|-|-|-|
|Alphapose|Fails to install alphapose due to some issue with required GPU|n/a|
|Google Media Pipe|Works the best with accuracy and improved speed|![Google Media Pipe Image 9](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/RESULTS-TOTAL/results_allImages_mediapipe/10.png?raw=true)|
|MMpose|Runs slow (likely due to no GPU) and accuracy struggles especially with hidden hands|![MediaPipe Image](https://github.com/Kunal2341/HandPosesAlgorithm/blob/master/RESULTS-TOTAL/results_allImages-mmpose/vis_009.jpg?raw=true)|


# Running Google Media Pipe
# Running MMPOSE
 To run the hands on mmpose 

1. Go within the mmpose folder
2. Running conda openmmlab use the following command 

```
conda activate openmmlab
```

3. For each file run the following thing 

```
python demo/top_down_img_demo_with_mmdet.py demo/mmdetection_cfg/cascade_rcnn_x101_64x4d_fpn_1class.py \
    cascade_rcnn_x101_64x4d_fpn_20e_onehand10k-dac19597_20201030.pth \
    configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py \
    res50_onehand10k_256x256-e67998f6_20200813.pth \
    --img-root tests/data/onehand10k/ \
    --img 9.jpg \
    --out-img-root testingResults \
    --device=cpu \
    --det-cat-id 1
``` 

`detcatid` can be either 0 or 1

Top-down approach
find two bounding boxes including each person
estimate human joint(15 key-point) per each bounding box
In this example, Top-down approach need pose estimation twice.

Bottom-up approach
estimate all human joint(30 key-point) in the picture
classify which joint(15 key-point) are included in the same person
In this example, pose estimator doesn't care how many people are in the picture. they only consider how they can classify each joint to the each person.

In general situation, Top-down approach consume time much more than Bottom-up, because Top-down approach need N-times pose estimation by person detector results.

## Old running for example images

Make sure you include 
```
--device cpu
```
```
python demo/bottom_up_img_demo.py associative_embedding_hrnet_w32_coco_512x512.py hrnet_w32_coco_512x512-bcb8c247_20200816.pth --img-path tests/data/coco/ --out-img-root vis_results --device cpu
```

## Other stuff
`python demo/top_down_img_demo.py     configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py     res50_onehand10k_256x256-e67998f6_20200813.pth     --img-root tests/data/onehand10k/ --json-file tests/data/onehand10k/test_onehand10k.json     --out-img-root vis_results     --device=cpu`


# Contact

I am Kunal Aneja, first year Computer Science student working on Pressure Vision project with Patrick Grady

@Kunal2341 -- kaneja6@gatech.edu



```python
def z_score_outliers(data, threshold=3):
    # Separate the x and y values into separate arrays
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    # Combine the x and y values into one array
    data = np.column_stack((x, y))
    # Compute the Z-scores for each point
    z_scores = np.abs(stats.zscore(data))
    # Identify the points that have Z-scores above the threshold
    outliers = np.where(z_scores > threshold)
    return outliers
```