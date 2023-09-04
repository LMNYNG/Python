import librosa
import librosa.display
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import glob
import sklearn
from keras import models, layers
from keras.preprocessing.image import ImageDataGenerator


audio_type = "포크"

pathL = glob.glob("음원/%s/*.wav" % audio_type)
sample_rate = 16000
dpi = 109.68
for path in pathL:
    filename = path.replace("\\","/").split("/")[2][:-4]

    audio = librosa.load(path, sr=sample_rate)[0]
    S = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=128)
    log_S = librosa.amplitude_to_db(S, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc = 1000, n_fft=400, hop_length=160)

    delta2_mfcc = librosa.feature.delta(mfcc, order=1)
    delta2_mfcc = sklearn.preprocessing.scale(delta2_mfcc, axis=1)

    plt.figure(figsize=(130/dpi, 131/dpi), dpi=dpi)
    librosa.display.specshow(delta2_mfcc, sr=16000 )


    plt.savefig('이미지/%s/%s.png' %(audio_type,filename),bbox_inches='tight')
