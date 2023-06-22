import torch
from trainModel import train_yolo

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    print("Cuda available: " + str(torch.cuda.is_available()))
    print("Num Devices: " + str(torch.cuda.device_count()))
    print("Device: " + str(torch.cuda.get_device_name()))
    train_yolo()