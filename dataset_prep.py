# Neccessary imports
import random
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras

# Process all of the data in `training_dataset`
def collect_bird_images():
    print("Collecting images...")
    image_list = []
    label_list = []

    # Open the classes, then navigate to bird image directory
    os.chdir('training_dataset')
    os.chdir('lists')
    classes = open('classes.txt', 'r')
    os.chdir('..')
    os.chdir('images')

    # Populate the image_list and label_list
    for directory in os.listdir(os.getcwd()):
        if directory[:1] != '.':
            for line in classes:
                os.chdir(line.strip())
                for image in os.listdir(os.getcwd()):
                    if image[:1] != '.':
                        label_list.append(0)
                        resize_image = Image.open(image).resize((128, 128))
                        grey_array = np.array(resize_image.convert('L'))
                        image_list.append(grey_array)
                os.chdir('..')
    classes.close()

    return [image_list, label_list]

def collect_landscape_images():
    image_list = []
    label_list = []

    # Populate the image_list and label_list
    os.chdir('..')
    os.chdir('landscape')
    for image in os.listdir(os.getcwd()):
        label_list.append(1)
        resize_image = Image.open(image).resize((128, 128))
        grey_array = np.array(resize_image.convert('L'))
        image_list.append(grey_array)
    os.chdir('..')
    os.chdir('..')

    print("\n...Images collected.")
    return [image_list, label_list]


# Split the data into training and testing datasets
def split_and_save_datasets():
    # Gather bird images and landscape images
    bird = collect_bird_images()
    landscape = collect_landscape_images()

    print("\nSplitting and saving datasets...")

    # Concatenate images and labels
    image_list = (bird[0] + landscape[0])
    label_list = (bird[1] + landscape[1])

    # Shuffle the datasets
    for _image in image_list:
        index = random.randint(0, len(image_list)-1)
        image = image_list.pop(index)
        image_list.append(image)
        label = label_list.pop(index)
        label_list.append(label)

    # Shorten dataset
    image_list = image_list[:6000]
    label_list = label_list[:6000]

    # Split and normalize the datasets
    split = round(len(label_list)/2)
    train_images = np.asarray(image_list[:split]) / 255.0
    test_images = np.asarray(image_list[len(image_list)-split:]) / 255.0
    train_labels = np.asarray(label_list[:split])
    test_labels = np.asarray(label_list[len(label_list)-split:])

    print(test_images.shape, train_images.shape, test_labels.shape, train_labels.shape)

    # Save the datasets
    np.save('test_images.npy', test_images)
    np.save('train_images.npy', train_images)
    np.save('test_labels.npy', test_labels)
    np.save('train_labels.npy', train_labels)

    print("\n...Datasets split and saved.")

