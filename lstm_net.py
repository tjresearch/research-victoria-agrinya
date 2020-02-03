#Victoria Agrinya
#Last update: 02.03.20

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras as k
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape, Embedding, Conv1D, GlobalMaxPooling1D, MaxPooling1D, Flatten, LSTM
import numpy as np
from resources import SongData, Track
import pickle

# songs = pd.read_excel(io="/Users/vicki/Documents/Senior_Research/Song Feature Data.xlsx", usecols=str)
#x_train, x_test = lists of mfcc values for each song; y_train, y_test = labels of popularity scores attributed to each list of mfcc data
uris = []
with open("Hot_100_uris.txt", "r") as infile:
    for i in infile.readlines():
        uris.append(str(i.strip()[14:]))

cols = ['mfcc', 'pop', 'tempo', 'valence', 'energy']
df = SongData(uris, cols)

# pickle df here!

# df.mfcc(uris)
# df.train_test()
# train = [df.x_train, df.y_train]
# save_train = open("train.pickle", "wb")
# pickle.dump(train, save_train)
# save_train.close()

read_train = open("train.pickle", "rb")
train = pickle.load(read_train)
read_train.close()

train_x = np.array(train[0])
train_y = np.array(train[1])
batch_size = len(train_x)
train_x = train_x.reshape(batch_size, 1292, 1)

# print(train_x)

model = Sequential() 
model.add(LSTM(units = 1, batch_input_shape = (None, 1292, 1)))
model.add(Dense(1))
model.add(Dense(1))
model.summary()
model.compile(optimizer = 'sgd', loss = 'mean_squared_error', metrics = ['accuracy'], sample_weight_mode=None, weighted_metrics=None, target_tensors=None)
model.fit(train_x, train_y, verbose = 2, epochs = 30)
model.predict()