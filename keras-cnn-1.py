#Victoria Agrinya
#Last update: 12.5.19

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras as k
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
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
print(len(mfcc))


# model = Sequential()
# model.add(Reshape((1,0), input_shape=(1000,)))
# model.add(Conv1D(100, 10, activation='relu', input_shape=(TIME_PERIODS, num_sensors)))
# model.add(Conv1D(100, 10, activation='relu'))
# model.add(MaxPooling1D(3))
# model.add(Conv1D(160, 10, activation='relu'))
# model.add(Conv1D(160, 10, activation='relu'))
# model.add(GlobalAveragePooling1D())
# model.add(Dropout(0.5))
# model.add(Dense(num_classes, activation='softmax'))
# print(model.summary())
