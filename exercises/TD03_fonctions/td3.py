#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnSeconde = temps[0] * 24 * 60 ** 2 + temps[1] * 60 ** 2 + temps[2] * 60 + temps[3]
    print(tempsEnSeconde)

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondeEnTemps = (temps[0] // (24 * 60 ** 2), (temps[0] % (24 * 60 ** 2) // 60 ** 2), ((temps[0] % (24 * 60 ** 2) % 60 ** 2)) // 60, \
        (((temps[0] % (24 * 60 ** 2) % 60 ** 2)) % 60) % 60)
    
temps = (secondeEnTemps(100000), 0, 0, 0)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

def afficheTemps(temps):
    """Renvoie le temps avec jour, heure, minute, seconde au pluriel ou non"""
    if temps[0] == 1 :
        print(temps[0], "jour", end=" ")
    elif temps[0] > 1 :
        print(temps[0], "jours", end=" ")
    if temps[1] == 1 :
        print(temps[1], "heure", end=" ")
    elif temps[1] > 1 :
        print(temps[1], "heures", end=" ")
    if temps[2] == 1 :
        print(temps[2], "minute", end=" ")
    elif temps[2] > 1 :
        print(temps[2], "minutes", end=" ")
    if temps[3] == 1 :
        print(temps[3], "seconde", end=" ")
    elif temps[3] > 1 :
        print(temps[3], "secondes", end=" ")

def demandeTemps():
    """Demande à l'utilisateur de rentrer un temps en jour, heure, minute, seconde"""
    global temps
    temps = (-1,0,0,0)
    while temps[0] == -1 or temps[1] >= 24 or temps[2] >= 60 or temps[3] >= 60 :
        temps = (int(input("entrez un temps en jour")),int(input("entrez un temps en heure")),int(input("entrez un temps en minute")),\
            int(input("entrez un temps en seconde")))
        if temps[1] >= 24 :
            print("erreur temps en heure >= 24 heures, entrez à nouveau le temps")
        if temps[2] >= 60 :
            print("erreur temps en minutes >= 60 minutes, entrez à nouveau le temps")
        if temps[3] >= 60 :
            print("erreur temps en seconde >= 60 secondes, entrez à nouveau le temps")
demandeTemps()
afficheTemps(temps)

def sommeTemps(temps1,temps2):
    """Calcule la somme de 2 temps"""
    sommeTemps = (temps1[0] + temps2[0], temps1[1] + temps2[1], temps1[2] + temps2[2], temps1[3] + temps2[3])
    print(sommeTemps)

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    """Renvoie le temps selon une certaine proportion donnée"""
    temps = temps[0] * proportion, temps[1] * proportion, temps[2] * proportion, temps[3] * proportion



afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments