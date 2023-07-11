import scipy.io.wavfile as wav
from playsound import playsound
import random

#imports data and normalizes data to -1 to 1
#outputs normalized signal and data rate
def getData(fileName):
    fs, signal = wav.read(fileName)
    return signal,fs

#plays sound and saves file
def play(sound,fs):
    wav.write('Voice Modulator/Scrambled.wav', fs, sound)
    playsound('Voice Modulator/Scrambled.wav')

#scrambles sound
def scramble(sound):
    max = sound.max()
    sound = sound/max

    for i,row in enumerate(sound):
        for j,entry in enumerate(row):
            sound[i][j] = entry + random.gauss(1,.1)