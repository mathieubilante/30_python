#compter  une lettre dans une mot ou phrase
print("Bienvenue dans le comptage de lettre")
lettre = input("Entrer la lettre à compter : ")
phrase = input("Entrer la phrase : ")
compteur = phrase.count(lettre)
print("La lettre", lettre, "apparaît", compteur, "fois dans la phrase.")