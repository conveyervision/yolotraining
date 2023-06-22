from ultralytics import YOLO

def run_yolo():
    model = YOLO('best.pt')
    results = model('')