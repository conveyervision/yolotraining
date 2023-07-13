# trainModel.py
from ultralytics import YOLO

def train_yolo(model_size='m', data='custom.yaml', epochs=10, imgsz=960, device=0, batch=10):
    if model_size.lower() == 'a':  # for all models
        model_sizes = ['x', 'l', 'm', 's', 'n']
    else:
        model_sizes = [model_size.lower()]

    for size in model_sizes:
        model = YOLO(f'yolov8{size}.pt')
        model.train(data=data, epochs=epochs, imgsz=imgsz, device=device, batch=batch)
