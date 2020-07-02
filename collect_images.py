# Neccessary imports 
from picamera import PiCamera
import os

print("This is a script to collect non-bird images of your local area, so as to get the model used its surroundings.")

# Starting point
start = input("Press and key to start.")

camera = PiCamera()

def most_recent(path):
    largest = 0
    for image in os.listdir(path):
        try:
            if image.split('.')[1] == 'jpg':
                image_number = int(image.split('.')[0])
                if image_number > largest:
                    largest = image_number
        except IndexError:
            pass
    return largest

print("Press 'enter' to take a picture. Press 'q' to exit the program.")

image_dir = '/home/pi/Pictures/local/'
flag = True
count = most_recent(image_dir)
while flag == True:
    pic_input = input(">>> ")
    if pic_input == "":
        count += 1
        print(f"Picture taken. Picture number: {count}")
        image_path = image_dir + str(count) + r'.jpg'
        camera.capture(image_path)
    elif pic_input == "q":
        print("Exiting...")
        flag = False
