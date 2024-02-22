
import math
lista=[]
with open("matriceint.py") as mat:
    for line in mat:
        splitted = line.split(",")
        new = []
        for a in splitted:
            new.append(int(a))
        lista.append(new)
        
    rows = len(lista)
    cols = len(lista[0])
    conta = 0
    while -math.inf <= (n := int(input("Se vuoi cercare un valore inseriscilo "))) <= math.inf:
        for x in range(cols):
            for y in range(rows):
                val = lista[y][x]
                if val == n:
                    conta+=1
                    print(f"Il valore {n} è presente in:")
                    print("Col: ", x, "Row: ", y)
        if conta == 0:
            print("Il valore non è nella lista")
       
    