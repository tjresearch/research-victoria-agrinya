#Victoria Agrinya
#Last updated: 12.5.19
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import librosa as lib

class Track:
    manager = SpotifyClientCredentials("8f408e92f7d24929ae7ac2613ebc11dc", "59dcf725c5494f7a8b31672ff4d46655")
    spo = spotipy.Spotify(client_credentials_manager = manager)
    play = spo.user_playlist("spotify:user:billboard.com", "spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ") 
    def __init__(self, id):
        self.uri = id
        self.features = spo.audio_features([id])[0]
    def getName(self):
        return self.spo.track(self.uri)["name"]
    def getArtist(self):
        return self.spo.track(self.uri)['album']['artists'][0]['name']
    def getDance(self):
        return self.features["danceability"]
    def getEnergy(self):
        return self.features["energy"]
    def getKey(self):
        return self.features["key"]
    def getLoudness(self):
        return self.features["loudness"]
    def getMode(self):
        return self.features["mode"]
    def getSpeechiness(self):
        return str(self.features["speechiness"])
    def getAcousticness(self):
        return str(self.features["acousticness"])
    def getInstrumentalness(self):
        return str(self.features["instrumentalness"])
    def getLiveness(self):
        return str(self.features["liveness"])
    def getValence(self):
        return str(self.features["valence"])
    def getTempo(self):
        return str(self.features["tempo"])
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
        self.li = []
        self.train = []
        self.test = []

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
            y, sr = lib.load("/Users/vicki/Documents/Senior_Research/Hot 100 MP3s/" + track.getArtist() + " - " + track.getName()+ ".mp3", duration=30)
            mfcc = lib.feature.mfcc(y=y,sr=sr, n_mfcc=5)
            self.li.append(mfcc[0:1000:1])
        return self.li

    def train_test(self):
        for i in range(50):
            track = Track(self.id[i])
            x_train, y_train = self.li[i], track.getPop() 
            self.train.append((x_train, y_train))
        
        for i in range(50, 100, 1):
            track = Track(self.id[i])
            x_test, y_test = self.li[i], track.getPop()
            self.test.append((x_test, y_test))

        return {"train": self.train, "test": self.test}
