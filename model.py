# Neccessary imports
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Build the model
def build_model():
    # Load the images and labels
    train_images = np.load('train_images.npy', allow_pickle=True)
    test_images = np.load('test_images.npy', allow_pickle=True)
    train_labels = np.load('train_labels.npy', allow_pickle=True)
    test_labels = np.load('test_labels.npy', allow_pickle=True)

    print(train_labels, test_labels)

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
    print("Test Accuracy:", test_accuracy)
    print("Test Loss:", test_loss)

    model.save('nn_model/model')

build_model()
