from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound = Sound(fileName= fileName)
sound.sound= sound.sound*5

sound.plotFourierTransform()

sound.play()
