#Victoria Agrinya
#Last updated: 12.9.19
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import librosa as lib

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
        self.li = []
        self.x_train = []
        self.y_train = []
        self.test = []
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
                y, sr = lib.load("/Users/vicki/Documents/Senior_Research/Hot 100 MP3s/" + track.getArtist() + " - " + track.getName()+ ".mp3", duration=30)
                mfcc = lib.feature.mfcc(y=y,sr=sr, n_mfcc=5)
                self.li.append(mfcc[0:1000:1])
                self.works.append(track)
            except FileNotFoundError:
                pass
        return self.li

    def train_test(self):
        for i in range(len(self.works)//2):
            track = self.works[i]
            self.x_train.append(self.li[i])
            self.y_train.append(track.getPop())
        
        for i in range(len(self.x_train)//2, len(self.x_train), 1):
            track = self.works[i]
            self.test.append(self.li[i], track.getPop())
            
