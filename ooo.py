X = int(input("entrer un nombre a rechercher : "))
n = int(input("entrer les nombres a saisis : "))
if n < 3 :
    while n < 3:
        n = int(input("entrer un un nombre superieur ou egal a 3 : "))

if n >= 3:
    nbrep = 0
    for c in range (1,n+1) :
        v = int(input("entrer une valeur : "))
        if X == v :
            nbrep += 1
            if nbrep == 1 :
                ppo = c
                print("La position de la premiere occurence est :",ppo)
            pdo = c
    if X != v and nbrep == 0:
        print("bonne chance a la prochaine")
    if  nbrep >= 1 :
        print("la position de la derniere occurence est :", pdo)

    if nbrep > 1:
        print("le nombre de repition est de",X,"est : ",nbrep)
    elif nbrep == 1:
        print("le nombre",X,"est affiche une seule fois il n'est pas repete, donc nombre de repition est 0")
