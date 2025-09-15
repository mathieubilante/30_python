print("Bienvenue dans l'affichage personnel")
nom =(input("entrer votrer nom :\n"))
prenom = (input("entrer votre prenom :\n"))
if  not nom.isalpha() or not prenom.isalpha():
    print("entrer une chaine de caractere")
else :
    majuscules = nom.upper()
    minuscules = prenom.lower()
    
#mes forme
print("Nom en majuscules est :\n", majuscules)
print("Prenom en minuscules est  : \n", minuscules)
#longeur total
longeurs = len((nom  + prenom).replace(" ",""))
print("La longeurs totale de vitre prenom et nom est : \n", Longeurs)
    