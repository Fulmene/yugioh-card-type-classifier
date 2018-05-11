import keras.backend as K
from keras.models import Sequential
from keras.layers import Embedding, Dense, Conv1D, MaxPooling1D, GlobalAveragePooling1D
from keras.preprocessing.sequence import pad_sequences

import numpy as np

import yugioh_data

def get_model(name_length=100, classes=3):
    model = Sequential()
    model.add(Embedding(len(yugioh_data.chars) + 1, 32))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(3))
    model.add(Conv1D(128, 3, activation='relu'))
    model.add(Conv1D(128, 3, activation='relu'))
    model.add(GlobalAveragePooling1D())
    model.add(Dense(3, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy'])

    return model

def str2arr(s):
    return list(map(yugioh_data.char2ind, s.lower()))

def preprocess_card_names(card_names, name_length=100):
    return np.array(pad_sequences(
               list(map(str2arr, card_names)),
               maxlen=name_length,
               padding='post',
               truncating='post'))

def preprocess_data(data):
    x = preprocess_card_names([d[0] for d in data])
    y = np.vectorize(yugioh_data.type2ind)([d[1] for d in data])
    return x, y

def predict(model, card_names):
    model.predict()
