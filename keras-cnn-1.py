#Victoria Agrinya
#Last update: 11.26.19

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
from resources import SongData
import pandas as pd

#dataframe data should be a list of lists, columns should be a list of strings, and dtype should be float

# songs = pd.read_excel(io="/Users/vicki/Documents/Senior_Research/Song Feature Data.xlsx", usecols=str)
x = [[-488.75186, 96, 110.56700, 0.34500, 0.68200],[-450.65536, 86, 88.96400, 0.28400, 0.47900], [-475.66257, 84, 82.33800, 0.28300, 0.28100]]
uris = ['6b2RcmUt1g9N9mQ3CbjX2Y']
cols = ['mfcc', 'pop', 'tempo', 'valence', 'energy']
df = SongData(uris, cols)
mfcc = df.mfcc(0)
for i in mfcc:
    print(i)

model = tf.keras.Sequential()
keras.layers.Conv1D(1, 1, strides=1, padding='valid', data_format='channels_last', dilation_rate=1, activation=None, 
use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, 
activity_regularizer=None, kernel_constraint=None, bias_constraint=None)

model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(layers.Conv2D(64, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(1000, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))
