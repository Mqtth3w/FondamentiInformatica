class Text:
    def __init__(self):
        self._listas = []
       
    def addtext(self, stringa):
        a = self._listas.append(stringa)
        return a

    def long_lines(self, soglia: int):
   
        numstrl = 0
        for stringa in self._listas:
            if len(stringa) >= soglia:
                numstrl += 1
        return numstrl

def main():
    t = Text()
    stringa = input("Digitare delle stringhe di testo ")
    while stringa != "":
       
        t.addtext(stringa)
        stringa = input("Digitare delle stringhe di testo ")
           
           
    soglia = int(input("Inserire una soglia "))
    while soglia > 0:
        n = t.long_lines(soglia)
        print(n)
        soglia = int(input("Inserire una soglia "))
       
main()