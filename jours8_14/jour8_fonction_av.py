#une fonction qui convertit des kilomètres en miles
def km_to_miles(km):
    mille = km * 0.621371
    return mille
km = float(input("Entrer la valeur en killometres ;"))
milles = km_to_miles(km)
print(f"{km} km = {milles} milles")
