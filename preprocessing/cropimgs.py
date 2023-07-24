import cv2

def crop_image(image_path, center_y, height=320):
    img = cv2.imread(image_path)
    img_height, img_width = img.shape[:2]

    center_y_pixel = int(center_y * img_height)
    upper_bound = max(0, center_y_pixel - height//2)
    lower_bound = min(img_height, center_y_pixel + height//2)

    cropped = img[upper_bound:lower_bound, :] # Crop the image
    cv2.imwrite(image_path.replace('.jpg', '_test.jpg'), cropped) # Save the image
