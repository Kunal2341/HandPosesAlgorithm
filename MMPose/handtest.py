# Copyright (c) OpenMMLab. All rights reserved.
import os
import warnings
from argparse import ArgumentParser

import mmcv
from xtcocotools.coco import COCO

from mmpose.apis import (inference_top_down_pose_model, init_pose_model, vis_pose_result)
from mmpose.datasets import DatasetInfo


"""
python demo/top_down_img_demo.py \
    configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py \
    https://download.openmmlab.com/mmpose/top_down/resnet/res50_onehand10k_256x256-e67998f6_20200813.pth \
    --img-root tests/data/onehand10k/ --json-file tests/data/onehand10k/test_onehand10k.json \
    --out-img-root vis_results

"""


pose_config = "configs/hand/2d_kpt_sview_rgb_img/topdown_heatmap/onehand10k/res50_onehand10k_256x256.py "
pose_checkpoint = "hrnet_w32_coco_512x512-bcb8c247_20200816.pth"
img_root=''
json_file = "tests/data/onehand10k/test_onehand10k.json",
show=False
out_img_root = ''
device='cuda:1'
kpt_thr=0.3
radius=4
thickness=1,
        


coco = COCO(json_file)
# build the pose model from a config file and a checkpoint file
pose_model = init_pose_model(
    pose_config, pose_checkpoint, device=device.lower())

dataset = pose_model.cfg.data['test']['type']
dataset_info = pose_model.cfg.data['test'].get('dataset_info', None)
if dataset_info is None:
    warnings.warn(
        'Please set `dataset_info` in the config.'
        'Check https://github.com/open-mmlab/mmpose/pull/663 for details.',
        DeprecationWarning)
else:
    dataset_info = DatasetInfo(dataset_info)

img_keys = list(coco.imgs.keys())

# optional
return_heatmap = False

# e.g. use ('backbone', ) to return backbone feature
output_layer_names = None

# process each image
for i in mmcv.track_iter_progress(range(len(img_keys))):
    # get bounding box annotations
    image_id = img_keys[i]
    image = coco.loadImgs(image_id)[0]
    image_name = os.path.join(img_root, image['file_name'])
    ann_ids = coco.getAnnIds(image_id)

    # make person bounding boxes
    person_results = []
    for ann_id in ann_ids:
        person = {}
        ann = coco.anns[ann_id]
        # bbox format is 'xywh'
        person['bbox'] = ann['bbox']
        person_results.append(person)

    # test a single image, with a list of bboxes
    pose_results, returned_outputs = inference_top_down_pose_model(
        pose_model,
        image_name,
        person_results,
        bbox_thr=None,
        format='xywh',
        dataset=dataset,
        dataset_info=dataset_info,
        return_heatmap=return_heatmap,
        outputs=output_layer_names)

    if out_img_root == '':
        out_file = None
    else:
        os.makedirs(out_img_root, exist_ok=True)
        out_file = os.path.join(out_img_root, f'vis_{i}.jpg')

    vis_pose_result(
        pose_model,
        image_name,
        pose_results,
        dataset=dataset,
        dataset_info=dataset_info,
        kpt_score_thr=kpt_thr,
        radius=radius,
        thickness=thickness,
        show=show,
        out_file=out_file)

