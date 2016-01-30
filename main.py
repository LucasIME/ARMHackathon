import math
import time
import socket
import pickle
from scipy import arange
from Speaker import *
import commands
from config import *

def main():
	# s = socket.socket()
	# s.bind((host, port))
	# s.listen(5)
	# c, addr = s.accept()

    # startTime = time.time()

    SpeakersList = [SpeakerA, SpeakerB, SpeakerC, SpeakerD]
    target = Object3D(9.2, 7.2, 3.9)

    cppRawOutput = commands.getstatusoutput("./cppCalculations %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s"
                                         % (speedOfSound, SpeakerA.x, SpeakerA.y, SpeakerA.z, SpeakerB.x, SpeakerB.y, SpeakerB.z, SpeakerC.x, SpeakerC.y, SpeakerC.z, SpeakerD.x, SpeakerD.y, SpeakerD.z, target.x, target.y, target.z, iStart, iStop, jStart, jStop, kStart, kStop ))
    finalCoordinates = [ float(numberString) for numberString in cppRawOutput[1].split() ]

    finalPointOut = Object3D(finalCoordinates[0], finalCoordinates[1], finalCoordinates[2])

    # finalTime = time.time() - startTime;
    # print finalTime

    print finalPointOut
    
    # c.send(pickle.dumps(finalPointOut))
    # c.close()

if __name__ == '__main__':
    main()
