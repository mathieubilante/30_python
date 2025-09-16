#les liste,turples et methode
fruits=["pomme","banane","orange","kiwi"]
fruits.append("mangue")   # ajoute à la fin
fruits.insert(1, "kiwi")  # insère à l’index 1
fruits.remove("banane")   # supprime l’élément
fruits.pop()              # retire le dernier
fruits.sort()             # tri alphabétique
fruits.reverse()          # inverse l’ordre
print(len(fruits))           # longueur
for fruit in fruits :
    print(fruit)




courses = []
nb_artcle= int(input("combien d'arctcle vous vouer  ajouter  :"))
# Ajouter 5 articles
for i in range(n):
    article = input(f"Entrez l'article {i+1} : ")
    courses.append(article)

print("\nListe de courses :", courses)

# Supprimer un article
sup = input("Quel article voulez-vous supprimer ? ")
if sup in courses:
    courses.remove(sup)
    print("Liste mise à jour :", courses)
else:
    print("Article non trouvé.")
