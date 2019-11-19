#Victoria Agrinya
#Last update: 11.12.19

from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os
from keras.datasets import boston_housing as bh
import pandas as pd

songs = pd.read_excel(io="/Users/vicki/Documents/Senior_Research/Song Feature Data.xlsx", usecols=str)
b = pd.DataFrame()
print(songs)

class SongData:
    
    def __init__(self):
        super().__init__()
        self.dict = {}
        self.df = pd.DataFrame()
