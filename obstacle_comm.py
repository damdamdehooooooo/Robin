import Ed
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.ObstacleDetectionBeam(Ed.ON)

while True:

    obstacle = Ed.ReadObstacleDetection()

    # 🧱 OBSTACLE DETECTÉ
    if obstacle == Ed.OBSTACLE_AHEAD or obstacle == Ed.OBSTACLE_RIGHT or obstacle == Ed.OBSTACLE_LEFT:
    
        Ed.SendIRData(1)
        Ed.Drive(Ed.STOP, Ed.SPEED_1, 10)
        

    else:

        DataIR = Ed.ReadIRData()

        # 📡 message reçu → stop
        if DataIR == 1:
            Ed.Drive(Ed.STOP, Ed.SPEED_1, 10)

        # 🚗 rien reçu → avancer
        elif DataIR == 0:
            Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 1)

        # 🔁 fallback
        else:
            Ed.SendIRData(1)
            Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 1)