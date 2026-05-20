import Ed

Ed.EdisonVersion = Ed.V3
Ed.Tempo = Ed.TEMPO_SLOW
Ed.DistanceUnits = Ed.TIME


Ed.LineTrackerLed(Ed.ON)

Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 1000)
while True:

    if Ed.ReadLineState() == Ed.LINE_ON_BLACK:
        Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 10)
    else:
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_1, 10)
        
        
Ed.LineTrackerLed(Ed.OFF)