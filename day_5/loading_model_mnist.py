from keras import models
from keras.datasets import mnist

# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
model = models.load_model('../model/digit-model')
print(type(model))
print(model.name)
print(model.dtype)
