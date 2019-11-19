#Victoria Agrinya
#Updated: 11.14.19

import librosa
import matplotlib.pyplot as plt
import os

li = os.listdir('/Users/vicki/Documents/Senior_Research/Hot 100 MP3s')

# with open("/Users/vicki/Documents/Senior_Research/Hot 100 mfccs", "w") as outfile:
#     for i in li:
#         y, sr = librosa.load("/Users/vicki/Documents/Senior_Research/Hot 100 MP3s/" + i)
#         mfcc = librosa.feature.mfcc(y=y, sr=sr)
#         outfile.write(i + str(mfcc[0]))
#         print("done")
#         outfile.write("\n")

for i in range(len(li)):
    print(li[i])


#Graph MFCC time series
# plt.figure(figsize=(10, 4))
# librosa.display.specshow(mf2, x_axis='time')
# plt.colorbar()
# plt.title("California Dreamin' (Original)")
# plt.tight_layout()
# plt.show()
