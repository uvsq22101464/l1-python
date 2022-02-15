carre_mag = [4, 14, 15, 1, 9, 7, 6, 12, 5, 11, 10, 8, 16, 2, 3, 13]
carre_pas_mag = [4, 14, 15, 1, 9, 7, 6, 12, 5, 11, 10, 8, 16, 2, 7, 13]

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    cpt = -1
    for i in range(4) :
        for j in range(4) :
            cpt += 1
            print(carre[cpt], end=' ')
        print('')

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    cpt = 0
    liste_somme = []
    for i in range(4) :
        somme = carre[cpt] + carre[cpt + 1] + carre[cpt + 2] + carre[cpt + 3]
        cpt += 4
        liste_somme.append(somme)
    if len(set(liste_somme)) == 1 :
        return somme
    else :
        return -1

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    cpt = 0
    liste_somme = []
    for i in range(4) :
        somme = carre[cpt] + carre[cpt + 4] + carre[cpt + 8] + carre[cpt + 12]
        cpt += 1
        liste_somme.append(somme)
    if len(set(liste_somme)) == 1 :
        return somme
    else :
        return -1

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    cpt = 0
    liste_somme = []
    for i in range(2) :
        somme = carre[cpt] + carre[cpt + 5] + carre[cpt + 10] + carre[cpt + 15]
        cpt = -cpt
        liste_somme.append(somme)
    if len(set(liste_somme)) == 1 :
        return somme
    else :
        return -1

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) != -1 and testColonnesEgales(carre) != -1 and testDiagonalesEgales != -1 :
        return True

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    for i in range(len(carre)) :
        if len(carre) == i ** 2 :
            return True

afficheCarre(carre_mag)