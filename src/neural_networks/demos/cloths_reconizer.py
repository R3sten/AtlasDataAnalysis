import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_labels),(test_images, test_labels) = fashion_mnist.load_data()

plt.imshow(train_images[0])
plt.show()
# print(train_labels[0])
# print(train_images[0])

# training_images = train_images/255.0
# test_images = test_images/255.0

# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28,28)),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])

# model.compile(optimizer=tf.train.AdamOptimizer(),loss='sparse_categorical_crossentropy')

# model.fit(train_images, train_labels, epochs=5)

# test_loss, test_acc = model.evaluate(test_images,test_labels)

# predictions = model.predict()