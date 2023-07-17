from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound, fs = importSound(fileName= fileName)
sound= sound*5

plotFourierTransform(sound)
play(sound,fs)
