import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft #using fft
import math
from scipy.io.wavfile import read
from config import wavFileName

LIMIT = 15000
CONSEQUITIVE = 3

WAIT_SAMPLES = 3000
WINDOW_MAX = 300
END_REACHED = 200000

def detection(array_of_samples):
    flag = 0
    for x in range(0, len(array_of_samples) - len(array_of_samples)%64, 64):
        fft_of_samples = array_of_samples[x:x+64]
        fft_of_samples = fft(fft_of_samples)
        fft_of_samples = [ abs(j) for j in fft_of_samples ]
        fft_of_samples = fft_of_samples[0:32]

        if flag > 0:
            if fft_of_samples[12] > LIMIT:
                flag += 1
            else:
                flag = 0                            #Carry on searching afresh

        if flag == 0 and (fft_of_samples[12] > LIMIT):
            # If we enter here we think we've detected the arrival of a pulse.
            # BUT to confirm it's not just noise we take a few more subsequent chunks and analyse them to see for sure
            Timestamp_Pulse = x
            flag = 1
            old_chunk = x / 64

        if flag == CONSEQUITIVE:                               #We're pretty sure now that we've just received a pulse not just noise
            return (Timestamp_Pulse)

    return(END_REACHED)


def getTimesList():
    Time_of_Pulse = []
    Number_of_Pulses = 0

    (sampling_rate, array_2) = read(wavFileName)
    #array = [ x[0] for x in array_2]
    array = array_2

    Temp = detection(array)
    if Temp == END_REACHED:
        print("No pulses detected.")
        return([])

    Time_of_Pulse.append(Temp)
    array = array[(Time_of_Pulse[0] + WAIT_SAMPLES):]
    Time_of_Pulse[0] /= 44.1

    for x in range(1, 8):
        Temp = detection(array)
        Number_of_Pulses = x
        if Temp == END_REACHED:
            break

        Time_of_Pulse.append(Temp)
        array = array[(Time_of_Pulse[x] + WAIT_SAMPLES):]
        Time_of_Pulse[x] /= 44.1
        Time_of_Pulse[x] += Time_of_Pulse[x - 1] + (WAIT_SAMPLES / 44.1)

    #------------
    print(Number_of_Pulses)
    if Number_of_Pulses < 5:
        print("This is not enough pulses!")
        return([])

    for x in range(1, Number_of_Pulses):
        TimeDiff = Time_of_Pulse[x] - Time_of_Pulse[x - 1]
        if (TimeDiff > WINDOW_MAX and (Number_of_Pulses >= x + 3)):  #When we find the first pulse
            # print(Time_of_Pulse[x])
            # print(Time_of_Pulse[x+1] - 200)
            # print(Time_of_Pulse[x+2] - 400)
            # print(Time_of_Pulse[x+3] - 600)
            responseVector = [ Time_of_Pulse[x], Time_of_Pulse[x+1] - 200, Time_of_Pulse[x+2] - 400, Time_of_Pulse[x+3] - 600 ]

            responseVector_Test = responseVector
            responseVector_Test.sort()
            if(responseVector_Test[3] - responseVector_Test[0] > 50):
                return([])
            return responseVector
    return([])