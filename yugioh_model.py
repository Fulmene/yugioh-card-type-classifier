import keras.backend as K
from keras.models import Sequential
from keras.layers import Embedding, Dense, Dropout, Conv1D, MaxPooling1D, Flatten
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

import numpy as np

import yugioh_data

def get_model(name_length=60, classes=3):
    model = Sequential()
    model.add(Embedding(len(yugioh_data.chars) + 1, 32, input_length=name_length))
    model.add(Dropout(0.2))
    model.add(Conv1D(128, 5, activation='relu'))
    model.add(Conv1D(128, 5, activation='relu'))
    model.add(MaxPooling1D())
    model.add(Dropout(0.5))
    model.add(Conv1D(128, 5, activation='relu'))
    model.add(Conv1D(128, 5, activation='relu'))
    model.add(MaxPooling1D())
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(classes, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])

    return model

def str2arr(s):
    return list(map(yugioh_data.char2ind, s.lower()))

def preprocess_card_names(card_names, name_length=60):
    return np.array(pad_sequences(
               list(map(str2arr, card_names)),
               maxlen=name_length,
               padding='post',
               truncating='post'))

def preprocess_data(data):
    x = preprocess_card_names([d[0] for d in data])
    y = to_categorical(np.vectorize(yugioh_data.type2ind)([d[1] for d in data]), num_classes=3)
    return x, y

def predict(model, card_names):
    return model.predict(preprocess_card_names(card_names))
