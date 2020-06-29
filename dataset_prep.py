# Neccessary imports
import random
import os
import numpy as np
from PIL import Image

# Process all of the data in `training_dataset`
def collect_bird_images():
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
                        resize_image = Image.open(image).resize((256, 256))
                        grey_array = np.array(resize_image.convert('L'))
                        image_list.append(grey_array)
                os.chdir('..')

    return [image_list, label_list]

def collect_landscape_images():
    image_list = []
    label_list = []

    # Populate the image_list and label_list
    os.chdir('..')
    os.chdir('landscape')
    for image in os.listdir(os.getcwd()):
        label_list.append(1)
        resize_image = Image.open(image).resize((256, 256))
        grey_array = np.array(resize_image.convert('L'))
        image_list.append(grey_array)
    os.chdir('..')
    os.chdir('..')

    return [image_list, label_list]


# Split the data into training and testing datasets
def split_datasets():
    # Gather bird images and landscape images
    bird = collect_bird_images()
    landscape = collect_landscape_images()

    # Concatenate images and labels
    image_list = bird[0] + landscape[0]
    label_list = bird[1] + landscape[1]

    # Split and normalize the datasets
    midpoint = round(len(label_list)/2)
    test_images = np.asarray(image_list[:midpoint]) / 255.0
    train_images = np.asarray(image_list[len(image_list)-midpoint:])
    test_labels = np.asarray(label_list[:midpoint]) / 255.0
    train_labels = np.asarray(label_list[len(label_list)-midpoint:])

    return [test_images, train_images, test_labels, train_labels]

# Save the datasets to .npy files
def save_dataset():
    dataset = split_datasets()
    np.save('test_images.npy', dataset[0])
    np.save('train_images.npy', dataset[1])
    np.save('test_labels.npy', dataset[2])
    np.save('train_labels.npy', dataset[3])

save_dataset()


