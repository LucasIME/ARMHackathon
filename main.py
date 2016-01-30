import math
import time
import socket
import pickle
from scipy import arange
from Speaker import *
import commands

def finalPoint(pointList):
	finalX = 0.0
	finalY = 0.0
	finalZ = 0.0
	weight = 0.0
	for pair_in in pointList[0:len(pointList)/10]:
		finalX += pair_in[1].x * (1/pair_in[0])
		finalY += pair_in[1].y * (1/pair_in[0])
		finalZ += pair_in[1].z * (1/pair_in[0])
		weight += 1/pair_in[0]
	final = Object3D((finalX / weight),(finalY / weight),(finalZ / weight))
	return final
	
def multilateration_thread( SpeakersList,  iStart, iStop, jStart, jStop, kStart, kStop, distAB, distBC, distAC, distAD, distBD, distCD):
    fPointList = []
    stepIterationLength = 0.3
    for i in arange(iStart, iStop, stepIterationLength):
        for j in arange (jStart, jStop, stepIterationLength):
            for k in arange(kStart, kStop, stepIterationLength):
                currentPoint = Object3D(i,j,k)
                distToSpeakerA = currentPoint.distanceTo(SpeakersList[0])
                distToSpeakerB = currentPoint.distanceTo(SpeakersList[1])
                distToSpeakerC = currentPoint.distanceTo(SpeakersList[2])
                distToSpeakerD = currentPoint.distanceTo(SpeakersList[3])
                testAB  = distToSpeakerA - distToSpeakerB
                testBC  = distToSpeakerB - distToSpeakerC
                testAC  = distToSpeakerA - distToSpeakerC
                testAD  = distToSpeakerA - distToSpeakerD
                testBD  = distToSpeakerB - distToSpeakerD
                testCD  = distToSpeakerC - distToSpeakerD
                accuracy = math.sqrt( ((distAB - testAB)**2) + ((distBC - testBC)**2) + ((distAC - testAC)**2) + ((distAD - testAD)**2) + ((distBD -  testBD)**2) + ((distCD - testCD)**2) )
                if accuracy <= 1.0:
                    entry = (accuracy, currentPoint)
                    fPointList.append(entry)
    return fPointList

def main():
	# s = socket.socket()
	# host = '172.23.72.51'
	# port = 1337
	# s.bind((host, port))
	# s.listen(5)
	# c, addr = s.accept()
    # startTime = time.time()
    speedOfSound = 343
    SpeakerA = Speaker(0, 0, 0)
    SpeakerB = Speaker(10, 0, 0)
    SpeakerC = Speaker(0, 20, 0)
    SpeakerD = Speaker(5, 10, 5)
    SpeakersList = [SpeakerA, SpeakerB, SpeakerC, SpeakerD]
    target = Object3D(9.2, 7.2, 3.9)

    iStart = 0.0
    iStop = 10.0
    jStart = 0.0
    jStop = 20.0
    kStart = 0.0
    kStop = 5.0

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
