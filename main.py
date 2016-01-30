import math
import time
import socket
import pickle
from scipy import arange
from Speaker import *
from multiprocessing.pool import ThreadPool

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
    pool = ThreadPool(processes=1)
    speedOfSound = 343
    SpeakerA = Speaker(0, 0, 0)
    SpeakerB = Speaker(10, 0, 0)
    SpeakerC = Speaker(0, 20, 0)
    SpeakerD = Speaker(5, 10, 5)
    SpeakersList = [SpeakerA, SpeakerB, SpeakerC, SpeakerD]
    target = Object3D(9.2, 7.2, 3.1)

    #Calculating needed constants
    timeA = target.distanceTo(SpeakerA) / speedOfSound
    timeB = target.distanceTo(SpeakerB) / speedOfSound
    timeC = target.distanceTo(SpeakerC) / speedOfSound
    timeD = target.distanceTo(SpeakerD) / speedOfSound
    timeAB = timeA - timeB
    timeBC = timeB - timeC
    timeAC = timeA - timeC
    timeAD = timeA - timeD
    timeBD = timeB - timeD
    timeCD = timeC - timeD
    distAB  = timeAB * speedOfSound
    distBC  = timeBC * speedOfSound
    distAC  = timeAC * speedOfSound
    distAD  = timeAD * speedOfSound
    distBD  = timeBD * speedOfSound
    distCD  = timeCD * speedOfSound

    #assign 3 threads to do the multilateration calculation on different ranges
    thread1 = pool.apply_async( multilateration_thread, (SpeakersList, 0.0, 10.0, 0.0, 7.0, 0.0, 5.0, distAB, distBC, distAC, distAD, distBD, distCD,) )
    thread2 = pool.apply_async( multilateration_thread, (SpeakersList, 0.0, 10.0, 7.0, 14.0, 0.0, 5.0, distAB, distBC, distAC, distAD, distBD, distCD,) )
    thread3 = pool.apply_async( multilateration_thread, (SpeakersList, 0.0, 10.0, 14.0, 20.0, 0.0, 5.0, distAB, distBC, distAC, distAD, distBD, distCD,) )
    thread1Return = thread1.get(timeout=3)
    thread2Return = thread2.get(timeout=3)
    thread3Return = thread3.get(timeout=3)
    pointList = thread1Return + thread2Return + thread3Return
    pointList.sort()
    finalPointOut = finalPoint(pointList)
    print finalPointOut

    #c.send(finalPoint(pointList))


if __name__ == '__main__':
    main()
