import scipy.io.wavfile as wav
import Functions

def getData(fileName):
    fs, signal = wav.read(fileName)
    signal = signal / 32767 # 2**15 - 1