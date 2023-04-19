import tensorflow.keras as keras



class EpochResponse(keras.callbacks.Callback):
    def __init__(self, epoch, model):
        self.epoch = epoch
        self.model = model


    def on_start(self, epoch, logs={}):
        if epoch == self.epoch:
            self.model.save_weights('model.h5')


    def on_end(self, epoch, logs={}):
        if epoch == self.epoch:
            self.model.save_weights('model.h5')
