#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

from typing import Counter


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0] * 24 * 60 ** 2 + temps[1] * 60 ** 2 + temps[2] * 60 + temps[3]
    return seconde

temps = (3,23,1,34)
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps = (seconde // (24 * 60 ** 2), (seconde % (24 * 60 ** 2) // 60 ** 2), ((seconde % (24 * 60 ** 2) % 60 ** 2)) // 60, \
        (((seconde % (24 * 60 ** 2) % 60 ** 2)) % 60) % 60)
    return temps
    
temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

def afficheTemps(temps):
    """Renvoie le temps avec jour, heure, minute, seconde au pluriel ou non"""
    if temps[0] > 0 and temps[0] <= 1 :
        print(temps[0], "jour", end=" ")
    elif temps[0] > 1 :
        print(temps[0], "jours", end=" ")
    if temps[1] > 0 and temps[1] <= 1 :
        print(temps[1], "heure", end=" ")
    elif temps[1] > 1 :
        print(temps[1], "heures", end=" ")
    if temps[2] > 0 and temps[2] <= 1 :
        print(temps[2], "minute", end=" ")
    elif temps[2] > 1 :
        print(temps[2], "minutes", end=" ")
    if temps[3] > 0 and temps[3] <= 1 :
        print(temps[3], "seconde", end=" ")
    elif temps[3] > 1 :
        print(temps[3], "secondes", end=" ")

def demandeTemps():
    """Demande à l'utilisateur de rentrer un temps en jour, heure, minute, seconde"""
    global temps
    temps = (int(input("entrez un temps en jour")),int(input("entrez un temps en heure")),int(input("entrez un temps en minute")),\
            int(input("entrez un temps en seconde")))
    while temps[1] >= 24 or temps[2] >= 60 or temps[3] >= 60 :
        if temps[1] >= 24 :
            print("erreur temps en heure >= 24 heures, entrez à nouveau le temps")
        if temps[2] >= 60 :
            print("erreur temps en minutes >= 60 minutes, entrez à nouveau le temps")
        if temps[3] >= 60 :
            print("erreur temps en seconde >= 60 secondes, entrez à nouveau le temps")
        temps = (int(input("entrez un temps en jour")),int(input("entrez un temps en heure")),int(input("entrez un temps en minute")),\
            int(input("entrez un temps en seconde")))
    return temps
afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    """Calcule la somme de 2 temps"""
    sommeTemps = (temps1[0] + temps2[0], temps1[1] + temps2[1], temps1[2] + temps2[2], temps1[3] + temps2[3])
    return sommeTemps

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    """Renvoie le temps selon une certaine proportion donnée"""
    temps = (temps[0] * proportion, temps[1] * proportion, temps[2] * proportion, temps[3] * proportion)
    return temps


afficheTemps(proportionTemps((2,0,36,0),0.2))

def tempsEnDate(temps):
    """année jour heure minute"""
    global date
    année = 1970
    if temps[0] >= 365 :
        jours = temps[0] % 365 + 1
        année = temps[0] // 365 + 1970
    date = (année, jours, temps[1], temps[2], temps[3])
    return date

def afficheDate(temps) :
    global date
    tempsEnDate(temps)
    return date
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate(temps)

def bisextile(jour):
    année_bisextile = 2020
    global count
    count = 0
    for i in range(jour) :
        i = 2020 + i
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0 :
            print(i)
            count += 1
    return count
        
bisextile(20000)

def nombreBisextile(jour):
    global count
    bisextile(jour)
    return count

def tempsEnDateBisextile(temps):
    global date
    année = 1970
    if temps[0] >= 366 :
        jours = temps[0] // 365
        année = temps[0] % 365 + 1970
    date = (année, jours, temps[1], temps[2], temps[3])
    return date
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))

def verifie(liste_temps):
    mois1 = liste_temps[0][0] + liste_temps[0][1] + liste_temps[0][2] + liste_temps[0][3]
    mois2 = liste_temps[1][0] + liste_temps[1][1] + liste_temps[1][2] + liste_temps[1][3]
    mois3 = liste_temps[2][0] + liste_temps[2][1] + liste_temps[2][2] + liste_temps[2][3]
    mois4 = liste_temps[3][0] + liste_temps[3][1] + liste_temps[3][2] + liste_temps[3][3]
    if mois1 <= 140 and mois2 <= 140 and mois3 <= 140 and mois4 <= 140 :
        print("Ok.")
    else :
        print("Trop d'heures au total")

liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)