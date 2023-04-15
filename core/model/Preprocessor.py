import nltk
import string
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class Preprocessor:
    console = OutputConsole = None
    data = None
    max_length = None
    vocab_size = None
    tokenizer = None
    word_index = None
    train_sequences = None
    train_padded = None


    def __init__(self, data, max_length, vocab_size, console=None):
        """
            @Description: Preprocessor
            @Param: data: List[str]
            @Param: max_length: int
            @Param: vocab_size: int
            @Param: console: OutputConsole (optional)
                Display output to focused console
        """
        self.data = data
        self.max_length = max_length
        self.vocab_size = vocab_size


    def tokenize(self):
        """
            @Description: Tokenize
            @Params: None
            @Returns: None
        """
        if self.is_headless():
            print("Tokenizing...")
            self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=self.vocab_size, oov_token="<OOV>")
            self.tokenizer.fit_on_texts(self.data)
            self.word_index = self.tokenizer.word_index
            self.train_sequences = self.tokenizer.texts_to_sequences(self.data)
            self.train_padded = tf.keras.preprocessing.sequence.pad_sequences(self.train_sequences, maxlen=self.max_length, padding="post", truncating="post")
        else:
            self.console.print("Tokenizing...")
            self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=self.vocab_size, oov_token="<OOV>")
            self.console.print("Fitting on texts...")
            self.tokenizer.fit_on_texts(self.data)
            self.console.print("Getting word index...")
            self.word_index = self.tokenizer.word_index
            self.console.print("Getting train sequences...")
            self.train_sequences = self.tokenizer.texts_to_sequences(self.data)
            self.console.print("Getting train padded...")
            self.train_padded = tf.keras.preprocessing.sequence.pad_sequences(self.train_sequences, maxlen=self.max_length, padding="post", truncating="post")
            self.console.print("Done tokenizing.")
            self.console.print("")
            self.console.print("")



    def is_headless(self):
        return self.console is None


    def get_data(self):
        return self.train_padded


    def get_tokenizer(self):
        return self.tokenizer


    def get_word_index(self):
        return self.word_index
