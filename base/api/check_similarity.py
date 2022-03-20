import librosa
import librosa.display as display
import math

def cosine_similarity1(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)
  
def check_similarity(audio_path, audio_path2):
    # load audio files
    y1, sr1 = librosa.load(audio_path)
    y2, sr2 = librosa.load(audio_path2)
    # compute spectrogram for the audio files
    S1 = librosa.stft(y1)
    S2 = librosa.stft(y2)
    # convert to power spectrogram
    S_db = librosa.amplitude_to_db(abs(S1))
    S2_db = librosa.amplitude_to_db(abs(S2))
    # display spectrogram
    # display.specshow(S_db, y_axis='linear', x_axis='time', sr=sr, hop_length=512)
    # display.specshow(S2_db, y_axis='linear', x_axis='time', sr=sr2, hop_length=512)
    # plt.show()
    # compute cosine similarity
    return cosine_similarity1(S_db.flatten(), S2_db.flatten())