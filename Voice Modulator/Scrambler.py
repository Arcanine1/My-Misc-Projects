from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound, fs = getData(fileName)
plot(sound)
scramble(sound)
play(sound,fs)

