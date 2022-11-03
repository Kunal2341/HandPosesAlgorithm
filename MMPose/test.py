import os
from mmpose.apis import (init_pose_model, inference_bottom_up_pose_model, vis_pose_result)



config_file = 'associative_embedding_hrnet_w32_coco_512x512.py'
checkpoint_file = 'hrnet_w32_coco_512x512-bcb8c247_20200816.pth'
pose_model = init_pose_model(config_file, checkpoint_file, device='cuda:0')  # or device='cuda:0'

folderName = os.path.join(os.path.dirname(os.getcwd()), "random_images_duplicate")


print(os.path.exists(folderName))
print(folderName)

IMAGE_FILES = []
for img in os.listdir(folderName):
    IMAGE_FILES.append(folderName + "/" + img)



image_name = IMAGE_FILES[4]
print(image_name)
# test a single image
pose_results, _ = inference_bottom_up_pose_model(pose_model, image_name)

print(pose_results)

# show the results
vis_pose_result(pose_model, image_name, pose_results, out_file='demo/vis_persons.jpg')


