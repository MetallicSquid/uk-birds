# Neccessary imports
import tensorflow as tf
from tensorflow import keras
import numpy as np
import picamera
from time import sleep
from datetime import date
import os
from PIL import Image

# Create a predictor model to take photo when bird is detected
json_file = open("models/basic.json", "r")
loaded_json = json_file.read()
json_file.close()
model = tf.keras.models.model_from_json(loaded_json)
model.load_weights("models/basic.h5")

prob_model = tf.keras.Sequential([model,
    tf.keras.layers.Softmax()])

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

camera = picamera.PiCamera()
date_string = str(date.today())
picture_count = most_recent(r'/home/pi/Pictures') + 1

# Main loop
while True:
    file_name = str(picture_count) + '.jpg'
    file_path = "/home/pi/Pictures/" + file_name
    camera.capture(file_path)
    resize_image = Image.open(file_path).resize((128, 128))
    grey_array = np.array(resize_image.convert('L')).reshape(1, 128, 128) / 255.0
    prediction = prob_model.predict(grey_array)
    if prediction[0][0] > prediction[0][1]:
        print(f"Bird: {prediction[0][0]} - Accepted.")
        picture_count += 1
    else:
        print(f"Non-bird: {prediction[0][1]} - Rejected.")
        os.remove(file_path)
