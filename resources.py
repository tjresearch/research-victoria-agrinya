#Victoria Agrinya
#Last updated: 11.19.19
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

# class SongData:
#     def __init__(self, uri):
#         super().__init__()
#         self.dict = {}
#         self.df = pd.DataFrame()
    
