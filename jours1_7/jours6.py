#LES BOUCLES
print("la boulce de fibonacci")
n= int(input("entre un nombre : "))
a, b = 0, 1
compteur = 0
while a < n:
    print(a, end=" ")
    a, b = b, a + b
    compteur += 1
print("\nLe nombre de termes de la suite de Fibonacci inférieurs à", n, "est :", compteur)