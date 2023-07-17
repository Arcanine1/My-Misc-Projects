from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound, fs = importSound(fileName= fileName)
sound = modulateSpeed(sound)
plot(sound)
play(sound,int(1.7*fs))
