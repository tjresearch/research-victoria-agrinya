#Victoria Agrinya
#Last updated: 01.06.20
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import librosa as lib
import numpy as np

class Track:
    manager = SpotifyClientCredentials("8f408e92f7d24929ae7ac2613ebc11dc", "59dcf725c5494f7a8b31672ff4d46655")
    spo = spotipy.Spotify(client_credentials_manager = manager)
    play = spo.user_playlist("spotify:user:billboard.com", "spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ") 
    def __init__(self, uri):
        self.uri = uri
        self.features = self.spo.audio_features([self.uri])
    def getName(self):
        return self.spo.track(self.uri)["name"]
    def getArtist(self):
        return self.spo.track(self.uri)['album']['artists'][0]['name']
    def getDance(self):
        return self.features[0]["danceability"]
    def getEnergy(self):
        return self.features[0]["energy"]
    def getKey(self):
        return self.features[0]["key"]
    def getLoudness(self):
        return self.features[0]["loudness"]
    def getMode(self):
        return self.features[0]["mode"]
    def getSpeechiness(self):
        return str(self.features[0]["speechiness"])
    def getAcousticness(self):
        return str(self.features[0]["acousticness"])
    def getInstrumentalness(self):
        return str(self.features[0]["instrumentalness"])
    def getLiveness(self):
        return str(self.features[0]["liveness"])
    def getValence(self):
        return str(self.features[0]["valence"])
    def getTempo(self):
        return str(self.features[0]["tempo"])
    def getPop(self):
        return self.spo.track(self.uri)['popularity']

class SongData:
    manager = SpotifyClientCredentials("8f408e92f7d24929ae7ac2613ebc11dc", "59dcf725c5494f7a8b31672ff4d46655")
    spo = spotipy.Spotify(client_credentials_manager = manager) 
       
    def __init__(self, uris, features):
        self.id = uris
        self.data = []
        self.df = pd.DataFrame()
        self.cols = features
        self.x_train = []
        self.y_train = []
        self.works = []

    def makeDF(self):
        for x in self.id:
            track = Track(x)
            features = self.spo.audio_features([x])[0]
            li = []
            for i in self.cols:
                if i == "mfcc":
                    try:
                        y, sr = lib.load("/Users/vicki/Documents/Senior_Research/Hot 100 MP3s/" + track.getName()+ ".mp3")
                        mfcc = lib.feature.mfcc(y=y, sr=sr)
                        li.append(mfcc[0][0])
                    except FileNotFoundError:
                        print("Song not found")
                elif i == "pop":
                    li.append(self.spo.track(x)['popularity'])
                else: 
                    li.append(features[i])
            self.data.append(li)
        self.df = pd.DataFrame(data = self.data, columns = self.cols, dtype = float, index = [i+1 for i in range(len(self.id))])
        return self.df
    
    def mfcc(self, uris):
        for i in uris:
            track = Track(i)
            try:
                #storing mfcc values
                y, sr = lib.load("/Users/vicki/Documents/Senior_Research/Hot 100 MP3s/" + track.getArtist() + " - " + track.getName()+ ".mp3", duration=30, dtype="float")
                mfcc = lib.feature.mfcc(y=y,sr=sr, n_mfcc=10)
                self.x_train.append(mfcc)
                self.works.append(track)
            except FileNotFoundError:
                pass
        self.x_train= np.expand_dims(self.x_train, axis=1)
        self.x_train= np.expand_dims(self.x_train, axis=1)
        return self.x_train

    def train_test(self):
        for i in range(len(self.works)):
            track = self.works[i]
            # self.x_train.append(self.x_train[i])
            self.y_train.append(track.getPop())
        #Got rid of "test" list, from now on will test using a subset of the training data
        self.y_train = np.expand_dims(y_train, axis=1)
        self.y_train = np.expand_dims(y_train, axis=1)
        
