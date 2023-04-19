import nltk
import string
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
from keras.preprocessing.text import Tokenizer



class Preprocessor:
    y_test = None
    y_train = None
    x_test = None
    x_train = None
    tokens = None


    def __init__(self, args):
        self.data = args.data
        self.data_max_length = args.max_length
        self.max_words = args.max_words
        self.test_size = args.test_size


    def preprocess(self):
        dataframe = pd.DataFrame(self.data, columns=['text', 'target'])
        X = dataframe['text'].values
        Y = dataframe['target'].values

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=self.test_size)


    def tokenize(self):
        self.tokens = Tokenizer(num_words=self.max_words)
        self.tokens.fit_on_texts(self.data)


    def sequence(self):
        self.x_train = self.tokens.texts_to_sequences(self.x_train)
        self.x_test = self.tokens.texts_to_sequences(self.x_test)
        self.x_train = tf.keras.preprocessing.sequence.pad_sequences(self.x_train, maxlen=self.data_max_length)
        self.x_test = tf.keras.preprocessing.sequence.pad_sequences(self.x_test, maxlen=self.data_max_length)
