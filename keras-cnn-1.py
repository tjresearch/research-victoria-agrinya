#Victoria Agrinya
#Last update: 01.14.20

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape, Embedding, Conv1D, GlobalMaxPooling1D, MaxPooling1D, Flatten
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
train_x = train_x.reshape(len(train_x), 1292, 1)
train_y = np.array(train[1])
print(len(train_y))

model = Sequential() 
model.add(Conv1D(1, (1), activation = 'softmax', input_shape = (1292, 1))) #add input shape if first layer
# input_shape: (# of timesteps/mfcc, # of features)
model.add(Reshape((1, 1))) #changes OUTPUT shape
# model.add(Conv1D(1, (1), activation = 'relu', input_shape = (1, 1)))
# model.add(Conv1D(1, (1), activation = 'relu', input_shape = (1, 1)))
# model.add(Activation('sigmoid'))
# model.add(Flatten())
# model.add(Dense(2, activation='sigmoid'))
# model.add(Dropout(0.2))
# model.add(MaxPooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last'))
model.compile(optimizer = 'sgd', loss = 'mean_squared_error', metrics = ['accuracy'], sample_weight_mode=None, weighted_metrics=None, target_tensors=None)
# model.fit(np.asfarray(train[0]), np.asfarray(train[1]), epochs=1, verbose=1, callbacks=None, validation_split=0.1, shuffle = True, steps_per_epoch=None, validation_freq=1, max_queue_size=10, workers=1, use_multiprocessing=False)
model.fit(train_x, train_y, verbose = 2, epochs = 5)
model.summary()
