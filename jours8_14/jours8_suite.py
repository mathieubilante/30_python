#les fonctions
n = int(input("entrer un nombre : "))
def table_de_multiplication (n) :
    print("   " , end= "")
    for k in range(1 , n+1) :
        print(f"{k : 4}", end= "")
    print("\n" + "--"*(4*(n+1)))
    for i in range(1 , n+1) :
        print(f"{i : 2}|", end= "")
        for j in range(1 , n+1) :
            print(f"{i*j : 4}", end= "")
        print()    
    return n
table_de_multiplication(n)

        