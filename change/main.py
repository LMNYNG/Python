#pip install pydub  
## install ffmpeg to your computer  
# apt-get install ffmpeg
from pydub import AudioSegment
import glob

audio_type = "포크b"

pathL = glob.glob("오디오/%s/*.mp3" % audio_type)
for path in pathL:
    filename = path.replace("\\","/").split("/")[2][:-4]

    dst = ("포크/%s.wav" %filename)

    # convert wav to mp3
    sound = AudioSegment.from_mp3(path)
    sound.export(dst, format="wav")