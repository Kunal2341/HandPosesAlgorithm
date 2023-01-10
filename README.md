# HandPosesAlgorithm


Fails to install alphapose due to some issue with required GPU
# use --device cpu


python demo/bottom_up_img_demo.py associative_embedding_hrnet_w32_coco_512x512.py hrnet_w32_coco_512x512-bcb8c247_20200816.pth --img-path tests/data/coco/ --out-img-root vis_results --device cpu



## To run the hands on mmpose 

within the mmpose folder

running conda openmmlab

python demo/top_down_img_demo.py     configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py     res50_onehand10k_256x256-e67998f6_20200813.pth     --img-root tests/data/onehand10k/ --json-file tests/data/onehand10k/test_onehand10k.json     --out-img-root vis_results     --device=cpu



python demo/top_down_img_demo_with_mmdet.py demo/mmdetection_cfg/cascade_rcnn_x101_64x4d_fpn_1class.py \
    cascade_rcnn_x101_64x4d_fpn_20e_onehand10k-dac19597_20201030.pth \
    configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py \
    res50_onehand10k_256x256-e67998f6_20200813.pth \
    --img-root tests/data/onehand10k/ \
    --img 9.jpg \
    --out-img-root testingResults \
    --device=cpu \
    --det-cat-id 1 


detcatid can be either 0 or 1

Top-down approach
find two bounding boxes including each person
estimate human joint(15 key-point) per each bounding box
In this example, Top-down approach need pose estimation twice.

Bottom-up approach
estimate all human joint(30 key-point) in the picture
classify which joint(15 key-point) are included in the same person
In this example, pose estimator doesn't care how many people are in the picture. they only consider how they can classify each joint to the each person.

In general situation, Top-down approach consume time much more than Bottom-up, because Top-down approach need N-times pose estimation by person detector results.



