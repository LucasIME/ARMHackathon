from Speaker import *

wavFileName = "4_8KHz_beep_Noise_Proper.wav"

host = '172.23.72.51'
port = 1337

SpeakerA = Speaker(0, 0, 0)
SpeakerB = Speaker(10, 0, 0)
SpeakerC = Speaker(0, 20, 0)
SpeakerD = Speaker(5, 10, 5)

speedOfSound = 343

iStart = 0.0
iStop = 10.0
jStart = 0.0
jStop = 20.0
kStart = 0.0
kStop = 5.0