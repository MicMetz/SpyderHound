import tensorflow as tf
from keras import Sequential
from keras.layers import LSTM, Dropout, BatchNormalization, Dense, GRU

from core.Model.AbstractModel import AbstractModel



class RecurrentModel(AbstractModel):
    def __init__(self, dataset):
        super().__init__(dataset)

        self.model = Sequential()
        self.model.add(LSTM(128, input_shape=(self.dataset.train_images.shape[1:]), activation='relu', return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(BatchNormalization())

        self.model.add(LSTM(128, activation='relu'))
        self.model.add(Dropout(0.1))
        self.model.add(BatchNormalization())

        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(10, activation='softmax'))

        optimizer = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

        self.model.compile(loss='sparse_categorical_crossentropy',
                           optimizer=optimizer,
                           metrics=['accuracy'])


    @property
    def name(self):
        return "Recurrent"


    @property
    def train(self):
        self.model.fit(self.dataset.train_images, self.dataset.train_labels, epochs=5)
        self.model.evaluate(self.dataset.test_images, self.dataset.test_labels)
        return self.model


    @property
    def predict(self):
        return self.model.predict(self.dataset.test_images)
