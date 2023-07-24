def adjust_bounding_boxes(file_path, center_y, height=320):
    with open(file_path, 'r') as f:
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
        if 0 <= center_y_new <= 1: # Check if it is still inside the image
            new_line = "{} {} {} {} {}\n".format(class_id, center_x, center_y_new, box_width, box_height)
            new_lines.append(new_line)

    with open(file_path.replace('.txt', '_test.txt'), 'w') as f:
        f.writelines(new_lines)
