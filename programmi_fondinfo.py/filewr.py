'''
esercizio 5.4
'''
'''
from random import randint
n = int(input("Inserire un numero "))
x,y=0,0
with open("lettura.py","w") as pos:
    for i in range(n):
        r = randint(0,3)
        if r == 0:
            y-=1
        elif r == 1:
            x+=1
        elif r == 2:
            y+=1
        elif r == 3:
            x-=1
        print(r,",",x,",",y, file=pos)
'''
'''
esercizio 5.5
'''
import math
def distance(p2: (float,float)) -> (float, float):
    x2, y2 = p2
    ea = math.sqrt((0-x2)**2+(0-y2)**2)
    return ea  

dirz=[0,0,0,0]
lista=[]
listad=[]
Euclide=0
with open("lettura.py","r") as pos:
    for a in pos:
        if a[0] == "0":
            dirz[0]+=1
            
        elif a[0] == "1":
            dirz[1]+=1
            
        elif a[0] == "2":
            dirz[2]+=1
            
        elif a[0] == "3":
            dirz[3]+=1
            
    print("Alto:",dirz[0]," Destra:",dirz[1]," Basso:",dirz[2]," Sinistra:",dirz[3])
    
with open("lettura.py","r") as pos:
    for b in pos:
        p = b.split()
        new=[]
        p[0] = []
        for i in p:
            if i != "," and i != []:
                new.append(float(i))
        fl = (new[0], new[1])
        lista.append(fl)
 
    for c in lista:
        k = distance(c)
        if k >= Euclide:
            Euclide=k
    print("La distanza euclidea del punto più lontano dall'origine è: ",Euclide)

'''
risultato del 5.4
2 , 0 , 1
2 , 0 , 2
2 , 0 , 3
2 , 0 , 4
0 , 0 , 3
2 , 0 , 4

esercizio 6.3
'''
'''
import math
def distance(p1: (float,float), p2: (float, float)) -> (float, float):
    x1, y1 = p1
    x2, y2 = p2
    ea = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return ea  
        
lista=[]
listad=[]
with open("lettura.py","r") as pos:
    for b in pos:
        p = b.split()
        new=[]
        p[0] = []
        for i in p:
            if i != "," and i != []:
                new.append(float(i))
        fl = (new[0], new[1])
        lista.append(fl)
 
    maxdist=0
    for a in lista:
        for b in lista:
            k = distance(a,b)
            if k > maxdist:
                maxdist=k
                ai, bi = a, b    
    print(f"I punti tra loro più distanti sono {ai}, {bi} ")
    print("La distanza fra loro è: ",maxdist)
'''

                
             
                

        