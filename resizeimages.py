# resizeimages.py

import os
import cv2

def resize_image(file_path, output_dir, resolutions):
    img = cv2.imread(file_path)
    if img is None:
        print(f'Error: Unable to open image file {file_path}')
        return

    original_height, original_width = img.shape[:2]
    aspect_ratio = original_width / original_height

    for resolution in resolutions:
        width = resolution
        height = int(width / aspect_ratio)
        resized_img = cv2.resize(img, (width, height))
        output_subdir = os.path.join(output_dir, f'{width}p')
        os.makedirs(output_subdir, exist_ok=True)
        base_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_subdir, base_name)
        cv2.imwrite(output_file_path, resized_img)

def resize_images_in_dir(input_dir, output_dir, resolutions):
    files = os.listdir(input_dir)
    for file in files:
        if file.endswith('.jpg'):
            resize_image(os.path.join(input_dir, file), output_dir, resolutions)
        elif file.endswith('.txt'):
            for resolution in resolutions:
                output_subdir = os.path.join(output_dir, f'{resolution}p')
                os.makedirs(output_subdir, exist_ok=True)
                base_name = os.path.basename(file)
                output_file_path = os.path.join(output_subdir, base_name)
                os.replace(os.path.join(input_dir, file), output_file_path)
