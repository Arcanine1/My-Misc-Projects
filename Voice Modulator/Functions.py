import scipy.io.wavfile as wav
import scipy.signal as signal
import scipy.fft as fft
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import random


class Sound():
    
    #imports data
    #supported types are wav
    #outputs signal and data rate
    def __init__(self,fileName):
        self.fs, self.sound = wav.read(fileName)

    #plays sound and saves file
    def play(self):
        wav.write('Voice Modulator/Scrambled.wav', self.fs, self.sound)
        playsound('Voice Modulator/Scrambled.wav')

    #Adds normally distributed noise sound
    #noise level is a positve number
    def addNoise(self,noiseLevel):

        if(noiseLevel<0):
            raise Exception ("Noise Level is negative")

        #adds some noise
        for i,row in enumerate(self.sound):
            for j,entry in enumerate(row):
                self.sound[i][j] = entry + random.gauss(0,entry*noiseLevel)
        
    #uses a low pass filter to make it low pitched
    def lowPitched(self,amount):

        if(amount<=0 or amount%1 !=0):
            raise Exception ("Amount is negative or 0 or non integer")

        convulutionMatrix = np.ones(amount)/amount

        for i in range(0,self.sound.shape[1]):
            self.sound[:,i] = signal.convolve(self.sound[:,i],convulutionMatrix,mode="same")
        


    #plots the sound
    def plot(self):
        import numpy as np
        time = np.linspace(0., 1, self.sound.shape[0])
        plt.plot(time, self.sound[:, 0], label="Left channel")
        plt.plot(time, self.sound[:, 1], label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()