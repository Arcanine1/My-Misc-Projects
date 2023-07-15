from Functions import *

fileName = "Voice Modulator/Spanish.wav"
sound = Sound(fileName= fileName)

sound.lowPitched(amount=30)
sound.play()
sound.plot()