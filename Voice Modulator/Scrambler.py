from Functions import *

fileName = "Voice Modulator/Music.wav"
sound, fs = importSound(fileName= fileName)
lowPitched(sound, amount=50)
sound = modulateSpeed(sound,5)

play(sound,int(1.75*fs))
