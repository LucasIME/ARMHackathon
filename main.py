import math
import time
import socket
import json
from scipy import arange
from Speaker import *
import commands
from config import *
from PulseDetection import getTimesList
from micController import getAndRecordAudio

def main():
    # s = socket.socket()
    # s.bind((host, port))
    # s.listen(5)
    # c, addr = s.accept()
    SpeakersList = [SpeakerA, SpeakerB, SpeakerC, SpeakerD]

    while(True):
        import os
        #getAndRecordAudio()

        timesList = getTimesList()
        if len(timesList) != 4:
            continue
        print timesList
        timeA = timesList[0]/1000
        timeB = timesList[1]/1000
        timeC = timesList[2]/1000
        timeD = timesList[3]/1000

        cppRawOutput = commands.getstatusoutput("./cppCalculations %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s"
                                             % (speedOfSound, SpeakerA.x, SpeakerA.y, SpeakerA.z, SpeakerB.x, SpeakerB.y, SpeakerB.z, SpeakerC.x, SpeakerC.y, SpeakerC.z, SpeakerD.x, SpeakerD.y, SpeakerD.z, timeA, timeB, timeC, timeD, iStart, iStop, jStart, jStop, kStart, kStop ))

        print(cppRawOutput)
        finalCoordinates = [ float(numberString) for numberString in cppRawOutput[1].split() ]

        finalPointOut = Object3D(finalCoordinates[0], finalCoordinates[1], finalCoordinates[2])

        print finalPointOut
        sendFinal = [finalPointOut.x, finalPointOut.y, finalPointOut.z]

        break

    #     c.send(json.dumps(sendFinal))
    # c.close()

if __name__ == '__main__':
    main()
