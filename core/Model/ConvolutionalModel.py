import tensorflow as tf
from keras import Sequential
from keras.layers import Flatten, Dense

from core.Model.AbstractModel import AbstractModel



class Convolutional(AbstractModel):
    def __init__(self, dataset):
        super().__init__(dataset)
        self.model = Sequential([
            Flatten(input_shape=(28, 28)),
            Dense(128, activation='relu'),
            Dense(10, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])


    @property
    def name(self):
        return "Convolutional"


    @property
    def train(self):
        self.model.fit(self.dataset.train_images, self.dataset.train_labels, epochs=5)
        self.model.evaluate(self.dataset.test_images, self.dataset.test_labels)
        return self.model
