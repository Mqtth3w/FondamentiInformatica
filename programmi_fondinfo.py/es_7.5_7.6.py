from boardgame import BoardGame
from boardgamegui import gui_play
from random import randint

class Numeri(BoardGame):
    def __init__(self, rc, minmax):
        self._righe, self._colonne = rc
        self._minimo, self._massimo = minmax
        self._matrix = []
        self._errori = 0
        for i in range(self._righe):
            for j in range(self._colonne):
                n = randint(self._minimo, self._massimo)
                self._matrix.append(n)
                
    def cols(self) -> int:
        return self._colonne
       
    def rows(self) -> int:
        return self._righe
           
    def value_at(self, x: int, y: int):
        m, w, h = self._matrix, self._righe, self._colonne
        if 0 <= y <= w and 0 <= x <= h and m[y * h + x] >= 0:
            if m[y * h + x] == 0:
                return ""
            return str(m[y * h + x])
        
   
    def play_at(self, x: int, y: int):
        w, h = self._righe, self._colonne
        if 0 <= y <= w and 0 <= x <= h:
            m, i = self._matrix, y * h + x
            if m[i] >= max(m):
                m[i] = 0
            else:
                self._errori+=1
                
    def flag_at(self, x: int, y: int):
        pass
    
    def message(self) -> (str):
        return f"Good guy! mistakes made: {self._errori}"
       
    def finished(self) -> bool:
        v = 0
        for i in self._matrix:
            if i == 0:
                v += 1
        if v == len(self._matrix):
            return True

def main():
    r = int(input("Righe?"))
    c = int(input("Colonne?"))
    smin = int(input("Soglia minima positiva?"))
    smax = int(input("Soglia massima positiva?"))
    game = Numeri((r,c),(smin,smax))
    gui_play(game)
   
main()