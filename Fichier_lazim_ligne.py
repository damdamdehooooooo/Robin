#-------------Setup----------------
import Ed

Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.LineTrackerLed(Ed.ON)

simple = Ed.TuneString(9, "c4g4G4D2z")
arret_effectue = False
compteur_gris = 0

while True:
    valeur_lumiere = Ed.ReadLineTracker()

    # 1. DÉTECTION DU NOIR (Tout ce qui est en dessous de 250)
    # On a remonté la limite pour capter les variations du noir
    if valeur_lumiere < 250:
        compteur_gris = 0
        arret_effectue = False
        Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)

    # 2. DÉTECTION DU GRIS (Tout ce qui est entre 250 et 500)
    # Pas besoin de réécrire "valeur > 250", car si le code arrive ici,
    # c'est obligatoirement que la valeur est de 250 ou plus !
    elif valeur_lumiere < 500:
        compteur_gris = compteur_gris + 1

        if compteur_gris > 700 and arret_effectue == False:
            Ed.Drive(Ed.STOP, Ed.SPEED_1, 0)
            Ed.PlayTune(simple)
            Ed.TimeWait(3000, Ed.TIME_MILLISECONDS)
            arret_effectue = True

        Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)

    # 3. DÉTECTION DU BLANC (Tout le reste, donc 500 et plus)
    else:
        compteur_gris = 0
        Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)