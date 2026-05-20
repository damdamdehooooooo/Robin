import Ed
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.ObstacleDetectionBeam(Ed.ON)

while True:

    obstacle = Ed.ReadObstacleDetection()
    
    if obstacle == Ed.OBSTACLE_AHEAD or obstacle == Ed.OBSTACLE_RIGHT or obstacle == Ed.OBSTACLE_LEFT  :
        Ed.Drive(Ed.BACKWARD, Ed.SPEED_1, 10)
        
    else:
        Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 1)
        
