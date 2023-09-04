import os
from multiprocessing import Pool
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import glob
import sklearn

pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i - a.shape[1]))))
dpi=109.68

def cal_data(file):
    fnameL = file.replace("\\", "/").split("/")
    print(file)
    audio, sr = librosa.load(file)
    S = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128)
    log_S = librosa.power_to_db(S, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=128, n_fft=400, hop_length=160)
    delta2_mfcc = librosa.feature.delta(mfcc, order=2)
    delta2_mfcc = sklearn.preprocessing.scale(delta2_mfcc, axis=1)
    padded_mfcc = pad2d(delta2_mfcc, 937)
    plt.figure(figsize=(130/dpi, 131/dpi), dpi=dpi)
    librosa.display.specshow(padded_mfcc)
    plt.savefig("이미지/%s/%s.png" % (fnameL[-2], fnameL[-1][:-4]), bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    with Pool(20) as p:
        for typeL in list(map(lambda x: glob.glob("음원/%s/*.wav" % x), ["포크","힙합","팝"])):
            p.map(cal_data,typeL)