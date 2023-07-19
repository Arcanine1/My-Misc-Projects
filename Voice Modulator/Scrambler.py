from Functions import *

fileName = "Voice Modulator/Music.wav"
sound, fs = importSound(fileName= fileName)
lowPitched(sound, amount=100)
sound = modulateSpeed(sound, amount = 100)
play(sound,int(1.6*fs))
