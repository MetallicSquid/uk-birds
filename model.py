# Neccessary imports
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Build the basic model
def build_basic():
    print("Building basic model...")
    # Load the images and labels
    train_images = np.load('data/train_images.npy', allow_pickle=True)
    test_images = np.load('data/test_images.npy', allow_pickle=True)
    train_labels = np.load('data/train_labels.npy', allow_pickle=True)
    test_labels = np.load('data/test_labels.npy', allow_pickle=True)

    # Form, compile and feed the model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(128, 128)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(2)
        ])

    model.compile(optimizer='adam',
            loss= tf.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
            )

    model.fit(train_images, train_labels, epochs=100)

    # Evaluate the accuracy of the model
    test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=2)
    print("\nTest Accuracy:", test_accuracy)
    print("Test Loss:", test_loss)

    # Save the model
    model.save('models/basic')
    print("\n...Basic model built.")

# Build the convolutional model
def build_conv():
    print("Building convolutional model...")
    # Load the images and labels
    train_images = np.load('data/train_images.npy', allow_pickle=True)
    test_images = np.load('data/test_images.npy', allow_pickle=True)
    train_labels = np.load('data/train_labels.npy', allow_pickle=True)
    test_labels = np.load('data/test_labels.npy', allow_pickle=True)

    # Reformat data for CNN
    row_num = train_images[0].shape[0]
    col_num = train_images[0].shape[1]
    train_images = train_images.reshape(train_images.shape[0], row_num, col_num, 1)
    test_images = test_images.reshape(test_images.shape[0], row_num, col_num, 1)

    # Form, compile and feed the model
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(row_num, col_num, 1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dense(2))

    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

    # Save the model
    model.save('models/convolutional')
    print('...Convolutional model built.')



