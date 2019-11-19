#Victoria Agrinya
#Last update: 11.07.19
#Last Hot 100 file update: 11.06.19

import spotipy
import librosa
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

#token = util.prompt_for_user_token("aurumlibro", "playlist-read-private", "8f408e92f7d24929ae7ac2613ebc11dc", "59dcf725c5494f7a8b31672ff4d46655", "https://www.spotify.com/us/")
manager = SpotifyClientCredentials("8f408e92f7d24929ae7ac2613ebc11dc", "59dcf725c5494f7a8b31672ff4d46655")
spo = spotipy.Spotify(client_credentials_manager = manager)

play = spo.user_playlist("spotify:user:billboard.com", "spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ") 
# print(play["tracks"]["items"][65]['track']['popularity'])

# with open("/Users/vicki/Documents/Senior_Research/Hot_100_uris.txt", 'w') as outfile:
#      for i in range(len(play["tracks"]["items"])):
#          outfile.write(str(play["tracks"]["items"][i]["track"]["uri"]))
#          outfile.write("\n")

# with open("/Users/vicki/Documents/Senior_Research/Hot_100_pop.txt", "w") as outfile:
#     for i in range(100):
#         outfile.write(str(play["tracks"]["items"][i]['track']['popularity']))
#         outfile.write("\n")
    #print(str(play["tracks"]["items"][i]["album"]['external_urls']['artists'][0]['external_urls']['external_ids']['spotify']))

# with open("/Users/vicki/Documents/Senior_Research/Hot_100_uris.txt", "r") as infile:
#     with open ("/Users/vicki/Documents/Senior_Research/Hot_100_Songs.txt", "w") as outfile:
#         for i in range(100): 
#             uri = infile.readline().strip()
#             outfile.write(spo.track(uri)["name"])
#             # outfile.write(spo.track(uri)["name"] + " by " + spo.track(uri)['album']['artists'][0]["name"])
#             outfile.write("\n")


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

li = ['6b2RcmUt1g9N9mQ3CbjX2Y', '0rKtyWc8bvkriBthvHKY8d', '454Epa1vrCGFddHXKyC1kb', '5KBARWIxeMGkvUax9VtVC9',
'3g9OCNXY2aSbGRQGY17qVE']
for i in li:
    print()
    t = Track(i)
    print(t.getName() + "'s" + " info:")
    print(str(t.getTempo()) + ", " + str(t.getValence()) + ", " + str(t.getEnergy()) + ", "+ str(t.getPop()))

'''Sam Smith - Dancing With A Stranger (with Normani).mp3
Joji - SLOW DANCING IN THE DARK.mp3
Kanye West - Water.mp3
Saweetie - My Type.mp3
Brantley Gilbert - What Happens In A Small Town.mp3'''
