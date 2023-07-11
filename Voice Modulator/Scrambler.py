from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound, fs = getData(fileName)
scramble(sound)
play(sound,fs)

