#manipules les formatage
nombre = int(input("Entrer un nombre :"))
for i in range(1, nombre + 1) :
    print(" "*(nombre - i) , end=" ")
    print("*"* (2*i - 1))
    
    
 #damier
n =int(input("entrer un nombre : "))
for i in range(n) :
    for j in range(n) :
        if (i + j )% 2 == 0 :
            print("#", end= " ")
        else :
            print(".", end= " ")
    print()               