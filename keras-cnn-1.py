#Victoria Agrinya
#Last update: 12.9.19

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras as k
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D, MaxPooling1D
import numpy as np
from resources import SongData, Track
import pandas as pd

#dataframe data should be a list of lists, columns should be a list of strings, and dtype should be float

# songs = pd.read_excel(io="/Users/vicki/Documents/Senior_Research/Song Feature Data.xlsx", usecols=str)
#x_train, x_test = lists of mfcc values for each song; y_train, y_test = labels of popularity scores attributed to each list of mfcc data
uris = []
with open("Hot_100_uris.txt", "r") as infile:
    for i in infile.readlines():
        uris.append(str(i.strip()[14:]))

cols = ['mfcc', 'pop', 'tempo', 'valence', 'energy']
df = SongData(uris, cols)

mfcc = df.mfcc(uris)
df.train_test()


model = Sequential() 
model.add(Conv1D(100, 10, activation='relu', input_shape = (1000, None)))
#model.add(Conv1D(100, 10, activation='relu'))
#model.add(MaxPooling1D(3))
# model.add(Conv1D(160, 10, activation='relu'))
# model.add(Conv1D(160, 10, activation='relu'))
#model.add(GlobalMaxPooling1D())
model.add(Dropout(0.1))
model.add(Dense(units = 46, activation='softmax'))
model.compile(optimizer = 'sgd, ', loss = 'mean-squared-error', metrics = 'accuracy')
model.fit(x = [df.x_train], y = [df.y_train], batch_size = 4, epochs=5, verbose=1, 
validation_data=df.test, shuffle = True, steps_per_epoch=1, validation_freq=5)
print(model.summary())
