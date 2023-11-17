import cv2

def setup_camera(webcam_index):
    cap = cv2.VideoCapture(webcam_index)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    return cap