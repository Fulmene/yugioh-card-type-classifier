import keras.backend as K
from keras.models import Model
from keras.layers import Input, Embedding, Dense, Dropout, Conv1D, MaxPooling1D, Flatten
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

import numpy as np

import yugioh_data

def get_model(name_length=60, classes=3):
    inputs = Input(shape=(name_length,))
    embedding = Embedding(len(yugioh_data.chars) + 1, 32)(inputs)
    dropout1 = Dropout(0.2)(embedding)
    conv1 = Conv1D(256, 5, activation='relu')(dropout1)
    conv2 = Conv1D(256, 5, activation='relu')(conv1)
    maxpooling1 = MaxPooling1D()(conv2)
    dropout2 = Dropout(0.5)(maxpooling1)
    conv3 = Conv1D(512, 5, activation='relu')(dropout2)
    conv4 = Conv1D(512, 5, activation='relu')(conv3)
    maxpooling2 = MaxPooling1D()(conv4)
    dropout3 = Dropout(0.5)(maxpooling2)
    flatten = Flatten()(dropout3)
    dense = Dense(512, activation='relu')(flatten)
    dropout4 = Dropout(0.5)(dense)
    outputs = Dense(classes, activation='softmax')(dropout4)

    model = Model(inputs=inputs, outputs=outputs)
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
