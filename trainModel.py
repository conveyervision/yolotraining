from ultralytics import YOLO

def train_yolo():
    model = YOLO('yolov8x.pt')
    model.train(data='custom.yaml', epochs=100, imgsz=960, device=0, batch=2)

