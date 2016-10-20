from Speaker import *

wavFileName = "DEMO.wav"

host = 'localhost'
port = 1337

# SpeakerA = Speaker(0.1, 3.25, 4)
# SpeakerB = Speaker(3, 0, 2.4)
# SpeakerC = Speaker(0, 0, 2.4)
# SpeakerD = Speaker(0.9, 1.1, 0.9)

SpeakerA = Speaker(0, 0, 20)
SpeakerB = Speaker(0, 20, 0)
SpeakerC = Speaker(20, 0, 0)
SpeakerD = Speaker(10, 10, 10)

target = Object3D(17.2, 5.8, 11.7)

speedOfSound = 343

iStart = 15.0
iStop = 20.0
jStart = 0.0
jStop = 10.0
kStart = 0.0
kStop = 20.0