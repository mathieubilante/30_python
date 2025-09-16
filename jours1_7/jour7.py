#boucle imbrique
for i in range(5) :
    for j in range(4):
        for k in range (3) :
            print(f"i={i}, j={j}, k={k}")



nombre_etoile=int(input("Entrer combien d'etoile vouler vous afficher ? :"))
for i in range(nombre_etoile) :
    for j in range(nombre_etoile) :
        print("*",end="")  
    print()              