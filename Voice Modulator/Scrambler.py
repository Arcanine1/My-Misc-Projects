from Functions import *

fileName = "Voice Modulator/Music.wav"
sound, fs = importSound(fileName= fileName)
lowPitched(sound, amount=100)
sound = modulateSpeed(sound, amount = 100)
lowPitched(sound, amount=100)
addNoise(sound= sound, noiseLevel= .6)
play(sound,int(random.gauss(1.5,.1)*fs))
