# Mini-calculatrice - Jour 2, initialisation

# Demander deux nombres à l'utilisateur
a = input("Entrez le premier nombre : ")
b = input("Entrez le deuxième nombre : ")

# Conversion en float pour accepter les décimaux
a = float(a)
b = float(b)

# Calculs
addition = a + b
multiplication = a * b
division_reelle = a / b            # division classique
division_entiere = a // b          # partie entière
reste = a % b                      # reste de la division

# Affichage des résultats
print("\n--- Résultats ---")
print(f"Addition          : {addition}")
print(f"Multiplication    : {multiplication}")
print(f"Division réelle   : {division_reelle}")
print(f"Division entière  : {division_entiere}")
print(f"Reste (modulo)    : {reste}")
