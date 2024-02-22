from boardgame import BoardGame
from gui3inarow import gui_play

class _3inarow(BoardGame):
    def __init__(self, rc):
        self._righe, self._colonne = rc
        self._matrix = ["-"] * (self._colonne * self._righe)
        self._solved = False
        self._ripetizioni = True
               
    def cols(self) -> int:
        return self._colonne
       
    def rows(self) -> int:
        return self._righe
           
    def value_at(self, x: int, y: int):
        m, w, h = self._matrix, self._righe, self._colonne
        if 0 <= y < w and 0 <= x < h:
            return str(m[y * h + x])
        return str(m[y * h + x])
       
    def play_at(self, x: int, y: int):
        w, h = self._righe, self._colonne
        if 0 <= y < w and 0 <= x < h:
            m, i = self._matrix, y * h + x
            if m[i] == "-":
                m[i] = "W"
            elif m[i] == "W":
                m[i] = "B"
            else:
                m[i] = "-"
        return m[i]
               
    def flag_at(self, x: int, y: int):
        pass
   
    def message(self) -> (str):
        return "Game won!"
    
    def finished(self) -> bool:
        bianco_row, nero_row, ripetizioni_row, r_row, row = 0, 0, 0, 0, 0
        bianco_col, nero_col, ripetizioni_col, r_col, col = 0, 0, 0, 0, 0
        m, cln, rig = self._matrix, self._colonne, self._righe
        if "-" in m:
            return False
        for a in range(0,rig):
            for b in range(0,cln):  
                if m[a * cln + b] == "W":
                    bianco_row += 1
                elif m[a * cln + b] == "B":
                    nero_row += 1
                if m[b * cln + a] == "W":
                    bianco_col += 1
                elif m[b * cln + a] == "B":
                    nero_col += 1
                if m[a * cln + b] == m[a-1 * cln + b]:
                    ripetizioni_row += 1
                if m[b * cln + a] == m[b-1 * cln + a]:
                    ripetizioni_col += 1
            if bianco_row == rig/2 and nero_row == rig/2:
                nero_row, bianco_row = 0, 0
                row += 1
            if bianco_col == cln/2 and nero_col == cln/2:
                nero_col, bianco_col = 0, 0
                col += 1
            if ripetizioni_row > 1: 
                r_row += 1
            if ripetizioni_col > 1:
                r_col += 1
            #print(ripetizioni_row, ripetizioni_col)
            ripetizioni_row, ripetizioni_col = 0, 0
        if row == rig and col == cln:
            self._solved = True
        if r_row > self._righe or r_col > self._colonne:
            self._ripetizioni = False
        return self._solved and self._ripetizioni

def main():
    r, c = 4, 4
    '''
    with open("matriceint.py") as m:
        for line in m:
            r += 1
            c = len(line.split(","))'''

    game = _3inarow((r,c))
    gui_play(game)
    
main()

