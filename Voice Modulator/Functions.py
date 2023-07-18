import scipy.io.wavfile as wav
import scipy.signal as signal
import scipy.fft as fft
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import random
import math




#imports data
#supported types are wav
#outputs signal and data rate
def importSound(fileName):
    fs, sound = wav.read(fileName)
    return sound,fs

#plays sound and saves file
def play(sound,fs):
    wav.write('Voice Modulator/Scrambled.wav', fs, sound)
    playsound('Voice Modulator/Scrambled.wav')

#Adds normally distributed noise sound
#noise level is a positve number
def addNoise(sound,noiseLevel):

    if(noiseLevel<0):
        raise Exception ("Noise Level is negative")

    noise = np.random.normal(0,abs(noiseLevel*sound),size= sound.shape)
    sound = sound+noise
    return sound

#uses a low pass filter to make it low pitched
def lowPitched(sound,amount):

    if(amount<=0 or amount%1 !=0):
        raise Exception ("Amount is negative or 0 or non integer")

    convulutionMatrix = np.ones(amount)/amount

    for i in range(0,sound.shape[1]):
        sound[:,i] = signal.convolve(sound[:,i],convulutionMatrix,mode="same")
    


#plots the sound
def plot(sound):
    import numpy as np
    time = np.linspace(0., 1, sound.shape[0])
    plt.plot(time, sound[:, 0], label="Left channel")
    plt.plot(time, sound[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

def plotFourierTransform(sound):
    size= sound.shape
    halfSized = (size[0]//2,size[1])

    fourierTransform = np.zeros(size, dtype= complex)
    magnitudes = np.zeros(size)
    positveFrequencies = np.zeros(halfSized)


    for i in range(0,sound.shape[1]):
        fourierTransform[:,i] = fft.fft(sound[:,i])
        magnitudes[:,i] = np.abs(fourierTransform[:,i])
        positveFrequencies[:,i] = magnitudes[:halfSized[0],i]
    
    frequency = np.linspace(start= 0, stop= halfSized[0], num = halfSized[0])

    plt.plot(frequency, positveFrequencies[:, 0], label="Left channel")
    plt.plot(frequency, positveFrequencies[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("frequency")
    plt.ylabel("Multiple")
    plt.show()


def modulateSpeed(sound,amount):
    start = 0
    length =0
    for i in range (0,amount):
        #creates start and lenght of slowed down portion
        size= sound.shape[0]
        
        start = random.randint(start+length+1000, int(sound.shape[0]))
        length = int(random.gauss(size/5,size/10))

        if(start+length > size):
            return sound

        if(length<0):
            return sound

        sound = _slowDownFactor2(sound,start,length)
    
    return sound


def _slowDownFactor2(sound,start,length):
    #slows down by adding "average entry" inbetween each entry for range

    #saves entries from before and after
    before = sound[:start]
    middle= sound[start:start+length]
    after = sound[start+length:]
    averaged = np.zeros((length-1,middle.shape[1]), dtype= "int16")

    #creates averaged array by adding evrey 2 consecutive entries and diving by 2
    #also adds last entry
    lastEntry = [] 
    for i in range(0,sound.shape[1]):
        averaged[:,i] =  (middle[:-1,i] + middle[1:,i]) // 2
        lastEntry.append((middle[-1,i] + after[0,i])//2)
    averaged = np.vstack((averaged,lastEntry), dtype="int16")

    #combines averages and middle
    middle= [val for pair in zip(middle, averaged) for val in pair]

    #combines into sound array
    sound = np.concatenate((before,middle,after), dtype= "int16")
    return sound