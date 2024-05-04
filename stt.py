# importing libraries
'''
import whisper
from glob import glob
from pydub import AudioSegment
from pydub.playback import play
import sys 
import os
'''

'''
sys.path.append('C:/Users/- Amir/Desktop/NLP/audios')
import AlKursi
'''

## solve this issue!!
'''
# importing path folder that belongs to our .mp3
audio_path = ("C:/Users/- Amir/Desktop/NLP/audios/")
mp3 = [file for file in os.listdir(audio_path) if file.endswith('.mp3')]
'''
# what song do you wanna process
'''
song = ("C:/Users/- Amir/Desktop/NLP/audios/AlKursi.mp3")
'''

## solve this issue!!
'''
# let's seprate our song!
seprator_path = ("C:/Users/- Amir/Desktop/NLP")
import seprator
seprator.seprator(mp3)
'''

# which model do we wanna work with?
'''
model = whisper.load_model('medium')
'''
# turning it into 30 seconds
'''
audio = AudioSegment.from_file(song)
length = 30 * 1000
lst = []

while len(audio) > length:
    piece = audio[:length]
    lst.append(piece)
    audio = audio[length:]
    
if len(audio)>0:
    lst.append(audio)

for i, j in enumerate(lst):
    j.export(f'song number {i}.mp3', format='mp3')
'''

# now let's transcribe it!
'''
directory = ('C:/Users/- Amir/Desktop/NLP')
files = sorted(glob(os.path.join(directory, '**/*.mp3'), recursive=True))

path1 = ("C:/Users/- Amir/Desktop/NLP/song number 0.mp3")
path2 = ("C:/Users/- Amir/Desktop/NLP/song number 1.mp3")
path3 = ("C:/Users/- Amir/Desktop/NLP/song number 2.mp3")
path4 = ("C:/Users/- Amir/Desktop/NLP/song number 3.mp3")

paths = [path1, path2, path3, path4]
'''
# finally, let's stt our songs!
'''
for file in paths:
    audio = whisper.load_audio(file)
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    print(f'detected language is: {max(probs, key=probs.get)}')
    
    option = whisper.DecodingOptions(fp16=False)
    
    result = model.transcribe(file)
    print(result['text'])    
    
    song = AudioSegment.from_mp3(file)
    play(song)
    '''

# when the processing had ended, copy and paste it in a .json file to see correct words. specially when it's persian or arabic.