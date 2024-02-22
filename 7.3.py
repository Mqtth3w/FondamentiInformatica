'''
def prodotto(lista: list) -> float:
    if not lista:
        return 1
    
    return lista[0]*prodotto(lista[1:])
     
print(prodotto([7, 4, 8, 0, 1]))

'''

'''

5,5,6,17
11,6,6,6
4,16,9,8
'''
'''
 
from random import randint
lista=[]
with open("matriceint.py","w") as m:
    rows = int(input("Inserisci il numero di righe "))
    cols = int(input("Inserisci il numero di colonne "))
    sogliamin = int(input("Soglia minima? "))
    sogliamax = int(input("Soglia massima? "))
    for i in range(rows):
        for j in range(cols):
            j = randint(sogliamin,sogliamax)
            while (j in lista) == True:
                j = randint(sogliamin,sogliamax)
            lista.append(j)
            print(f"{j}", file=m, end=",")
        print(file=m)
'''

'''
91,65,37,86
68,22,85,85
15,55,22,96
64,64,39,36

lista=[]
row=1
with open("matriceint.py","r") as m:
    for line in m:
        splitted = [int(n) for n in line.split(",")]
        c = len(splitted)
        for e in range(c):
            v = splitted[e]
            if v in lista:
                print("Il numero ripetuto è:",v)
                print(f"In posizione col:{e+1}, row:{row}")
            lista.append(v)
        row+=1
        
'''   
                
        
