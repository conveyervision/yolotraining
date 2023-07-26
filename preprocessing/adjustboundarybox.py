import cv2

def adjust_bounding_boxes(txt_file_path, img_file_path, center_y, new_height=320):
    # Open the image and get its height
    img = cv2.imread(img_file_path)
    if img is None:
        print(f'Error: Unable to open image file {img_file_path}')
        return
    original_height = img.shape[0]

    with open(txt_file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        data = line.split()
        class_id = data[0]
        center_x = float(data[1])
        center_y_orig = float(data[2])
        box_width = float(data[3])
        box_height = float(data[4])

        # Adjust the Y center
        center_y_new = (center_y_orig - center_y) + 0.5

        # Convert the box height from percentage to absolute pixel value
        box_height_pixel = box_height * original_height

        # Adjust the box height as a percentage of the new image height
        box_height_new = box_height_pixel / new_height

        if 0 <= center_y_new <= 1:  # Check if it is still inside the image
            new_line = "{} {} {} {} {}\n".format(class_id, center_x, center_y_new, box_width, box_height_new)
            new_lines.append(new_line)

    with open(txt_file_path.replace('.txt', '_test.txt'), 'w') as f:
        f.writelines(new_lines)
