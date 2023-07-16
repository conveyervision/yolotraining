# main.py

from trainModel import train_yolo
from processVideo import process_video
from changeLabelClass import change_label_class
from imagestomp4 import convert_images_to_mp4

def main_menu():
    print("Welcome to YoloTraining!")
    print("Please choose an option from the menu below:")
    print("1. Train model")
    print("2. Process video")
    print("3. Change label class")
    print("4. Convert images to mp4")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        model_size = input("Enter model size (X/L/M/S/N or A for All, default is M): ")
        data = input("Enter data file name (default is 'custom.yaml'): ")
        epochs = int(input("Enter number of epochs (default is 10): "))
        imgsz = int(input("Enter image size (default is 960): "))
        batch = int(input("Enter batch size (default is 10): "))
        train_yolo(model_size, data, epochs, imgsz, device=0, batch=batch)
    elif choice == "2":
        video_path = input("Enter path to video file: ")
        process_video(video_path)
    elif choice == "3":
        change_label_class()
    elif choice == "4":
        image_folder = input("Enter image folder (default is 'testing_images'): ")
        video_name = input("Enter output video name (default is 'output.mp4'): ")
        fps = int(input("Enter frames per second (default is 5): "))
        convert_images_to_mp4(image_folder, video_name, fps)
    else:
        print("Invalid choice, please enter a valid option.")

if __name__ == '__main__':
    main_menu()
