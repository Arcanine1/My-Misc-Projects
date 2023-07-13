from Functions import *

fileName = "Voice Modulator/Test.wav"
sound, fs = getData(fileName)
sound=sound*5


sound = addNoise(sound,noiseLevel=.2)
sound = modulateVolume(sound,variance=.2, amount=10)
sound= lowPitched(sound,amount= 75)
sound= lowPitched(sound,amount= 75)




play(sound,fs)
plot(sound)
