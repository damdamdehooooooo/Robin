#-------------Setup----------------
import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.TIME
Ed.Tempo = Ed.TEMPO_SLOW

#--------Your code below-----------

# Faire avancer le robot pendant 10 secondes à faible vitesse
Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 10000)

# Stop propre
Ed.Drive(Ed.STOP, Ed.SPEED_1, 1)
# son 1
Ed.PlayTone(880, 200)

# pause (boucle simple)
for i in range(30000):
    pass

# son 2
Ed.PlayTone(660, 200)

for i in range(30000):
    pass

# son 3
Ed.PlayTone(880, 200)

for i in range(30000):
    pass

# son final
Ed.PlayTone(523, 300)

for i in range(4000):
    pass

Ed.PlayBeep()



# Faire avancer le robot pendant 10 secondes à faible vitesse
Ed.Drive(Ed.FORWARD, Ed.SPEED_1, 10000)

# Stop propre
Ed.Drive(Ed.STOP, Ed.SPEED_1, 1)