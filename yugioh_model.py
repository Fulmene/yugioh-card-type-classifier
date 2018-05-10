import keras.backend as K
from keras.models import Sequential
from keras.layers import Embedding, Dense, Conv1D, MaxPooling1D, GlobalAveragePooling1D

import numpy as np

import characters

def get_model(name_length=100, classes=3):
    model = Sequential()
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
    return np.fromiter(map(characters.char2ind, s.lower()), float)

def predict(model, card_names):
    model.predict()
