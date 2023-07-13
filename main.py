# menu.py
from trainModel import train_yolo
from runModel import run_yolo

def main_menu():
    print("Welcome to YoloTraining!")
    print("Please choose an option from the menu below:")
    print("1. Train model")
    print("2. Run model")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        model_size = input("Enter model size (X/L/M/S/N or A for All, default is M): ")
        data = input("Enter data file name (default is 'custom.yaml'): ")
        epochs = int(input("Enter number of epochs (default is 10): "))
        imgsz = int(input("Enter image size (default is 960): "))
        batch = int(input("Enter batch size (default is 10): "))
        train_yolo(model_size, data, epochs, imgsz, device=0, batch=batch)
    elif choice == "2":
        run_yolo()
    else:
        print("Invalid choice, please enter a valid option.")

if __name__ == '__main__':
    main_menu()
