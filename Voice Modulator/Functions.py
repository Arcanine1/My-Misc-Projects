import scipy.io.wavfile as wav
import scipy.signal as signal
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import random
import soundfile as sf

#imports data
#supported types are wav
#outputs signal and data rate
def getData(fileName):
    fs, signal = wav.read(fileName)
    return signal,fs

#plays sound and saves file
def play(sound,fs):
    wav.write('Voice Modulator/Scrambled.wav', fs, sound)
    playsound('Voice Modulator/Scrambled.wav')

#Adds normally distributed noise sound
#noise level is a positve number
def addNoise(sound,noiseLevel):

    if(noiseLevel<0):
        raise Exception ("Noise Level is negative")

    #adds some noise
    for i,row in enumerate(sound):
        for j,entry in enumerate(row):
            sound[i][j] = entry + random.gauss(0,entry*noiseLevel)
    
    return sound

#uses a low pass filter to make it low pitched
def lowPitched(sound,amount):

    if(amount<=0):
        raise Exception ("Amount is negative or 0")

    convulutionMatrix = np.ones(amount)/amount

    for i in range(0,sound.shape[1]):
        sound[:,i] = signal.convolve(sound[:,i],convulutionMatrix,mode="same")
    
    return sound

#modulates volume
def modulateVolume(sound,variance,amount):

    if(variance<0 or amount < 0):
        raise Exception ("Variance or amountis negative")
    
    totalLength = len(sound)
    for i in range(0,amount):
        #modulates volume by taking a random amount consecutive entries and multiplying by an amount
        length = round(random.gauss(250000,5000))
        if(length<0):
            length=0

        start = random.randint(0,totalLength-length)
        for i in range (start,start+length):
            for j,entry in enumerate(sound[i]):
                multiplier = random.gauss(1,variance)
                if(multiplier<0):
                    multiplier=0
                sound[i][j] = entry * multiplier
    
    return sound


#plots the sound
def plot(data):
    import numpy as np
    time = np.linspace(0., 1, data.shape[0])
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()