# Neccessary imports
import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.models import model_from_json

# Test loading and prediction functionality
json_file = open("models/basic.json", "r")
loaded_json = json_file.read()
json_file.close()
model = tf.keras.models.model_from_json(loaded_json)
model.load_weights("models/basic.h5")

prob_model = tf.keras.Sequential([model,
    tf.keras.layers.Softmax()])

test_images = np.load("data/test_images.npy")

predictions = prob_model.predict(test_images)
for i in range(30):
    print(predictions[i])
    plt.figure()
    plt.imshow(test_images[i])
    plt.colorbar()
    plt.grid(False)
    plt.show()
