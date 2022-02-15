def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    global L
    L = [2]
    while L[-1] != 1 :
        if n % 2 == 0 :
            n = n / 2
            L.append(n)
        else :
            n = n * 3 +1
            L.append(n)
    del(L[0])
    return L

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for n in range(n_max) :
        syracuse(n+2)
    if 1 in L :
        return  True

def tempsVol(n):
    """ Retourne le temps de vol de n """
    syracuse(n)
    print(len(L))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    for n in range(n_max) :
        n += 1
        tempsVol(n)

def plusGrandEntierAtteint(n_max) :
    global L
    global L1
    L1 = [0]
    for i in range(n_max) :
        if i == 1 or i == 0 :
            continue
        tempsVol(i)
        L.sort()
        L1.append(L[-1])
    L1.sort()
    print(L1[-1])
