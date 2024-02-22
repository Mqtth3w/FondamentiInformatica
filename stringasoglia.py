def long_lines(listas, soglia: int):
   
    numstrl = 0
    for stringa in listas:
        if len(stringa) >= soglia:
            numstrl += 1
    return numstrl

def main():
   
    listas = []
    stringa = input("Digitare delle stringhe di testo ")
    while stringa != "":

        listas.append(stringa)
        stringa = input("Digitare delle stringhe di testo ")
       
    soglia = int(input("Inserire una soglia "))
    while soglia > 0:
        n = long_lines(listas, soglia)
        print(n)
        soglia = int(input("Inserire una soglia "))
       
main()