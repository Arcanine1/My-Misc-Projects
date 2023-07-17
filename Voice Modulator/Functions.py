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

    #adds some noise
    for i,row in enumerate(sound):
        for j,entry in enumerate(row):
            sound[i][j] = entry + random.gauss(0,entry*noiseLevel)
    
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


def modulateSpeed(sound):

    #creates start and lenght of slowed down portion
    size= sound.shape[0]
    start = random.randint(0,size)
    length = int(random.gauss(size/3,size/10))

    if(start+length > size):
        overshoot = length+start -size
        start = start-overshoot -10

    if(length<0):
        return

    #slows down by adding "average entry" inbetween each entry for range
    a=0
    #saves entries from before and after
    before = sound[:start]
    middle= np.zeros((0,sound.shape[1]), dtype= "int16")
    after = sound[start+length:]
    while(a<length):
        current = []
        averaged = []
        #creates tuple of length number of channels that will be appended
        for i in range(0,sound.shape[1]):
            current.append(sound[a + start,i])
            averaged.append(int((sound[a+start,i] + sound[a+start+1,i])/2))

        middle = np.vstack((middle,current),dtype= "int16")
        middle = np.vstack((middle,averaged),dtype= "int16")
        a= a+1
        print(a/length)
    #concatonates it all together
    sound = np.concatenate((before,middle,after), dtype= "int16")
    return sound
    