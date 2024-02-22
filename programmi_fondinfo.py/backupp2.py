from boardgame import BoardGame
from gui3inarow import gui_play

class _3inarow(BoardGame):
    def __init__(self, dim):
        self._righe, self._colonne = dim
        self._matrix = []
        self._file = None
        if self._righe == 0:
            self._file = "testmatrix.py"
            self._righe, self._colonne = 6, 6
        elif self._righe == 6: self._file = "matrix6.py"
        elif self._righe == 8: self._file = "matrix8.py"
        elif self._righe == 10: self._file = "matrix10.py"
        elif self._righe == 12: self._file = "matrix12.py"
        elif self._righe == 14: self._file = "matrix14.py"
        elif self._righe == 18: self._file = "matrix18.py"
        with open(self._file) as f:
            for line in f:
                l = line.split(",")
                for v in l:
                    if v[-1] == "\n":
                        self._matrix.append(str(v[-2]))
                    else:
                        self._matrix.append(str(v))
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
            elif m[i] == "B":
                m[i] = "-"
    
    def reset(self):
        self._matrix = []
        with open(self._file) as f:
            for line in f:
                l = line.split(",")
                for v in l:
                    if v[-1] == "\n":
                        self._matrix.append(str(v[-2]))
                    else:
                        self._matrix.append(str(v))
        return self._matrix
    
    def solve_recursive(self, i: int) -> bool:
        self.automatic_color()  # mark all obvious cells
        if self.unsolvable(): return False  # unsolvable
        # find first undecided cell, starting from i
        while i < len(self._matrix) and self._matrix[i] != "-":
            i += 1
        if i < len(self._matrix):
            saved = self._matrix[:]  # save current status
            for color in ("B", "W"):
                self._matrix[i] = color
                if self.solve_recursive(i + 1):
                    return True
                self._matrix = saved  # backtracking
        return self.finished()
    
    
    def automatic_color(self):
        m, rig, cln = self._matrix, self._righe, self._colonne
        nero_row, bianco_row, c_bianco_row, c_nero_row = 0, 0, [], []
        nero_col, bianco_col, c_bianco_col, c_nero_col = 0, 0, [], []
        t_w_row, t_b_row, t_w_col, t_b_col = 0, 0, 0, 0
        trip_w_row, trip_b_row, trip_w_col, trip_b_col = [], [], [], []
        Srepet_w_row, Srepet_b_row, Srepet_w_col, Srepet_b_col = [], [], [], []
        Drepet_w_row, Drepet_b_row, Drepet_w_col, Drepet_b_col = [], [], [], []
        bianco_final, nero_final = [], [] 
        for a in range(0,rig): 
            for b in range(0,cln):
                #controllo righe
                if (m[a * cln + b] == "W"):
                    bianco_row += 1
                elif (m[a * cln + b] == "w"):
                    bianco_row += 1
                elif (m[a * cln + b] == "-"):
                    t_w_row += 1
                    c_bianco_row.append(a * cln + b)
                #controllo colonne
                if (m[b * cln + a] == "W"):
                    bianco_col += 1
                elif (m[b * cln + a] == "w"):
                    bianco_col += 1
                elif (m[b * cln + a] == "-"):
                    t_w_col += 1
                    c_bianco_col.append(b * cln + a)
                #controllo righe
                if (m[a * cln + b] == "B"):
                    nero_row += 1
                elif (m[a * cln + b] == "b"):
                    nero_row += 1
                elif (m[a * cln + b] == "-"):
                    t_b_row += 1
                    c_nero_row.append(a * cln + b)
                #controllo colonne
                if (m[b * cln + a] == "B"):
                    nero_col += 1
                elif (m[b * cln + a] == "b"):
                    nero_col += 1
                elif (m[b * cln + a] == "-"):
                    t_b_col += 1
                    c_nero_col.append(b * cln + a)
                
                if (a*rig+b)//rig == (a*rig+b-1)//rig == (a*rig+b-2)//rig:
                    #controllo righe
                    #caso w w - || b b -
                    if (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + b] == "-": Drepet_w_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "w"):
                        if m[a * cln + b] == "-": Drepet_w_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + b] == "-": Drepet_b_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "b"):
                        if m[a * cln + b] == "-": Drepet_b_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == "W" and m[a * cln + (b-2)] == "w"):
                        if m[a * cln + b] == "-": Drepet_w_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == "w" and m[a * cln + (b-2)] == "W"):
                        if m[a * cln + b] == "-": Drepet_w_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == "B" and m[a * cln + (b-2)] == "b"):
                        if m[a * cln + b] == "-": Drepet_b_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == "b" and m[a * cln + (b-2)] == "B"):
                        if m[a * cln + b] == "-": Drepet_b_row.append(a * cln + b)
                    #controllo colonne
                    #caso w w - || b b -
                    if (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[b * cln + a] == "-": Drepet_w_col.append(b * cln + a) 
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "w"):
                        if m[b * cln + a] == "-": Drepet_w_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[b * cln + a] == "-": Drepet_b_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "b"):
                        if m[b * cln + a] == "-": Drepet_b_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == "W" and m[(b-2) * cln + a] == "w"):
                        if m[b * cln + a] == "-": Drepet_w_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == "w" and m[(b-2) * cln + a] == "W"):
                        if m[b * cln + a] == "-": Drepet_w_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == "B" and m[(b-2) * cln + a] == "b"):
                        if m[b * cln + a] == "-": Drepet_b_col.append(b * cln + a)
                    elif (m[(b-1) * cln + a] == "b" and m[(b-2) * cln + a] == "B"):
                        if m[b * cln + a] == "-": Drepet_b_col.append(b * cln + a)
                    #controllo righe
                    #caso - b b || - w w
                    if (m[a * cln + b] == m[a * cln + (b-1)] == "W"):
                        if m[a * cln + (b-2)] == "-": Srepet_w_row.append(a * cln + (b-2)) 
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "w"):
                        if m[a * cln + (b-2)] == "-": Srepet_w_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "B"):
                        if m[a * cln + (b-2)] == "-": Srepet_b_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "b"):
                        if m[a * cln + (b-2)] == "-": Srepet_b_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == "W" and m[a * cln + (b-1)] == "w"):
                        if m[a * cln + (b-2)] == "-": Srepet_w_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == "w" and m[a * cln + (b-1)] == "W"):
                        if m[a * cln + (b-2)] == "-": Srepet_w_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == "B" and m[a * cln + (b-1)] == "b"):
                        if m[a * cln + (b-2)] == "-": Srepet_b_row.append(a * cln + (b-2))
                    elif (m[a * cln + b] == "b" and m[a * cln + (b-1)] == "B"):
                        if m[a * cln + (b-2)] == "-": Srepet_b_row.append(a * cln + (b-2))
                    # controllo colonne
                    #caso - w w || - b b
                    if (m[b * cln + a] == m[(b-1) * cln + a] == "W"):
                        if m[(b-2) * cln + a] == "-": Srepet_w_col.append((b-2) * cln + a) 
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "w"):
                        if m[(b-2) * cln + a] == "-": Srepet_w_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "B"):
                        if m[(b-2) * cln + a] == "-": Srepet_b_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "b"):
                        if m[(b-2) * cln + a] == "-": Srepet_b_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == "W" and m[(b-1) * cln + a] == "w"):
                        if m[(b-2) * cln + a] == "-": Srepet_w_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == "w" and m[(b-1) * cln + a] == "W"):
                        if m[(b-2) * cln + a] == "-": Srepet_w_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == "B" and m[(b-1) * cln + a] == "b"):
                        if m[(b-2) * cln + a] == "-": Srepet_b_col.append((b-2) * cln + a)
                    elif (m[b * cln + a] == "b" and m[(b-1) * cln + a] == "B"):
                        if m[(b-2) * cln + a] == "-": Srepet_b_col.append((b-2) * cln + a)
                    # controllo righe
                    # caso w - w || b - b
                    if (m[a * cln + b] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + (b-1)] == "-": trip_w_row.append(a * cln + (b-1)) 
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "w"):
                        if m[a * cln + (b-1)] == "-": trip_w_row.append(a * cln + (b-1))
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + (b-1)] == "-": trip_b_row.append(a * cln + (b-1))
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "b"):
                        if m[a * cln + (b-1)] == "-": trip_b_row.append(a * cln + (b-1))
                    elif (m[a * cln + b] == "W" and m[a * cln + (b-2)] == "w"):
                        if m[a * cln + (b-1)] == "-": trip_w_row.append(a * cln + (b-1))
                    elif (m[a * cln + b] == "w" and m[a * cln + (b-2)] == "W"):
                        if m[a * cln + (b-1)] == "-": trip_w_row.append(a * cln + (b-1))                    
                    elif (m[a * cln + b] == "B" and m[a * cln + (b-2)] == "b"):
                        if m[a * cln + (b-1)] == "-": trip_b_row.append(a * cln + (b-1))
                    elif (m[a * cln + b] == "b" and m[a * cln + (b-2)] == "B"):
                        if m[a * cln + (b-1)] == "-": trip_b_row.append(a * cln + (b-1))
                    #controllo colonne                      
                    # caso w - w || b - b
                    if (m[b * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[(b-1) * cln + a] == "-": trip_w_col.append((b-1) * cln + a) 
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "w"):
                        if m[(b-1) * cln + a] == "-": trip_w_col.append((b-1) * cln + a)
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[(b-1) * cln + a] == "-": trip_b_col.append((b-1) * cln + a)
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "b"):
                        if m[(b-1) * cln + a] == "-": trip_b_col.append((b-1) * cln + a)
                    elif (m[b * cln + a] == "W" and m[(b-2) * cln + a] == "w"):
                        if m[(b-1) * cln + a] == "-": trip_w_col.append((b-1) * cln + a)
                    elif (m[b * cln + a] == "w" and m[(b-2) * cln + a] == "W"):
                        if m[(b-1) * cln + a] == "-": trip_w_col.append((b-1) * cln + a)                    
                    elif (m[b * cln + a] == "B" and m[(b-2) * cln + a] == "b"):
                        if m[(b-1) * cln + a] == "-": trip_b_col.append((b-1) * cln + a)
                    elif (m[b * cln + a] == "b" and m[(b-2) * cln + a] == "B"):
                        if m[(b-1) * cln + a] == "-": trip_b_col.append((b-1) * cln + a)
            #controllo righe
            if bianco_row == rig/2 and rig/2 >= t_w_row:
                for G in c_bianco_row:
                    bianco_final.append(G)
            if nero_row == rig/2 and rig/2 >= t_b_row:
                for B in c_nero_row:
                    nero_final.append(B)
            bianco_row, nero_row = 0, 0
            t_w_row, t_b_row = 0, 0
            c_bianco_row, c_nero_row = [], []
            #controllo colonne
            if bianco_col == cln/2 and cln/2 >= t_w_col:
                for Q in c_bianco_col:
                    bianco_final.append(Q)
            if nero_col == cln/2 and cln/2 >= t_b_col:
                for K in c_nero_col:
                    nero_final.append(K)
            bianco_col, nero_col = 0, 0
            t_w_col, t_b_col = 0, 0
            c_bianco_col, c_nero_col = [], []
        for X in trip_w_row:
            if m[X] == "-":
                m[X] = "B"
        for Y in trip_b_row:
            if m[Y] == "-":
                m[Y] = "W"
        for F in trip_w_col:
            if m[F] == "-":
                m[F] = "B"
        for P in trip_b_col:
            if m[P] == "-":
                m[P] = "W"
        #colorazione - w w || - b b
        for L in Srepet_w_row:
            if m[L] == "-":
                m[L] = "B"
        for U in Srepet_b_row:
            if m[U] == "-":
                m[U] = "W"
        for S in Srepet_w_col:
            if m[S] == "-":
                m[S] = "B"
        for T in Srepet_b_col:
            if m[T] == "-":
                m[T] = "W"
        #colorazione w w - || b b -
        for J in Drepet_w_row:
            if m[J] == "-":
                m[J] = "B"
        for E in Drepet_b_row:
            if m[E] == "-":
                m[E] = "W"
        for O in Drepet_w_col:
            if m[O] == "-":
                m[O] = "B"
        for V in Drepet_b_col:
            if m[V] == "-":
                m[V] = "W"
        trip_w_row, trip_b_row = [], []
        trip_w_col, trip_b_col = [], []
        Srepet_w_row, Srepet_b_row = [], []
        Srepet_w_col, Srepet_b_col = [], []
        Drepet_w_row, Drepet_b_row = [], []
        Drepet_w_col, Drepet_b_col = [], []
        #colorazione colonne/righe intere
        for BF in bianco_final:
            m[BF] = "B"
        for NF in nero_final:
            m[NF] = "W"
        bianco_final, nero_final = [], []
        return self._matrix
    
    def unsolvable(self) -> bool:
        m, rig, cln, solve = self._matrix, self._righe, self._colonne, False
        bianco_row, nero_row, ripetizioni_row, r_row, row = 0, 0, 0, 0, 0
        bianco_col, nero_col, ripetizioni_col, r_col, col = 0, 0, 0, 0, 0
        r1, r2, c1, c2 = 0, 0, 0, 0
        if "-" in m:
            return False
        else:
            for a in range(0,rig): #rig
                for b in range(0,cln):
                    if (m[a * cln + b] == "W"):
                        bianco_row += 1
                    elif (m[a * cln + b] == "w"):
                        bianco_row += 1
                    elif (m[a * cln + b] == "B"):
                        nero_row += 1
                    elif (m[a * cln + b] == "b"):
                        nero_row += 1
                    if m[a * cln + b] == m[a-1 * cln + b]:
                        ripetizioni_row += 1
                    if (m[a * cln + b] == m[a-1 * cln + b] == m[a-2 * cln + b]) == "W" or "B":
                        r1 += 1
                if bianco_row == rig/2 and nero_row == rig/2:
                    nero_row, bianco_row = 0, 0
                    row += 1
                if ripetizioni_row > 1: 
                    r_row += 1
                if r1 > 0:
                    r2 += 1
                ripetizioni_row, r1 = 0, 0
                
            for c in range(0,rig): #cln
                for d in range(0,cln):
                    if (m[d * cln + c] == "W"):
                        bianco_col += 1
                    elif (m[d * cln + c] == "w"):
                        bianco_col += 1
                    elif (m[d * cln + c] == "B"):
                        nero_col += 1
                    elif (m[d * cln + c] == "b"):
                        nero_col += 1
                    if m[d * cln + c] == m[d-1 * cln + c]:
                        ripetizioni_col += 1
                    if m[d * cln + c] == m[d-1 * cln + c] == m[d-2 * cln + c]:
                        c1 += 1
                if bianco_col == cln/2 and nero_col == cln/2:
                    nero_col, bianco_col = 0, 0
                    col += 1
                if ripetizioni_col > 1:
                    r_col += 1
                if c1 > 0:
                    c2 += 1
                ripetizioni_col, c1 = 0, 0
                    
        if (row != rig) or (col != cln) or (r_row > rig) or (r_col > cln) or (r2 > 1) or (c2 > 1):
            solve = True
        return solve
    
    def flag_at(self, x: int, y: int):
        pass
   
    def message(self) -> (str):
        return "Game won!"
    
    def finished(self) -> bool:
        bianco_row, nero_row, ripetizioni_row, r_row, row = 0, 0, 0, 0, 0
        bianco_col, nero_col, ripetizioni_col, r_col, col = 0, 0, 0, 0, 0
        m, cln, rig = self._matrix, self._colonne, self._righe
        r1, r2, c1, c2 = 0, 0, 0, 0 #triple
        if "-" in m:
            return False
        for a in range(0,rig): #righe
            for b in range(0,cln):
                if (m[a * cln + b] == "W"):
                    bianco_row += 1
                elif (m[a * cln + b] == "w"):
                    bianco_row += 1
                elif (m[a * cln + b] == "B"):
                    nero_row += 1
                elif (m[a * cln + b] == "b"):
                    nero_row += 1
                if m[a * cln + b] == m[a-1 * cln + b]:
                    ripetizioni_row += 1
                if m[a * cln + b] == m[a-1 * cln + b] == m[a-2 * cln + b]:
                    r1 += 1
            if bianco_row == rig/2 and nero_row == rig/2:
                nero_row, bianco_row = 0, 0
                row += 1
            if ripetizioni_row > 1: 
                r_row += 1
            if r1 > 1:
                r2 += 1
            ripetizioni_row, r1 = 0, 0
            
        for c in range(0,rig): #colonne
            for d in range(0,cln):
                if (m[d * cln + c] == "W"):
                    bianco_col += 1
                elif (m[d * cln + c] == "w"):
                    bianco_col += 1
                elif (m[d * cln + c] == "B"):
                    nero_col += 1
                elif (m[d * cln + c] == "b"):
                    nero_col += 1
                if m[d * cln + c] == m[d-1 * cln + c]:
                    ripetizioni_col += 1
                if m[d * cln + c] == m[d-1 * cln + c] == m[d-2 * cln + c]:
                    c1 += 1
            if bianco_col == cln/2 and nero_col == cln/2:
                nero_col, bianco_col = 0, 0
                col += 1
            if ripetizioni_col > 0:
                r_col += 1
            if c1 > 1:
                c2 += 1
            ripetizioni_col, c1 = 0, 0
        
        if r2 > 1 or c2 > 1:
            return False
        if row == rig and col == cln:
            self._solved = True
        if (r_row > rig or r_col > cln) :
            self._ripetizioni = False
        return self._solved and self._ripetizioni

def main():
    dim = int(input("Dimensione del puzzle: 6, 8, 10, 12, 14, 18? "))
    level = [0,6,8,10,12,14,18]
    if dim not in level:
        raise NotImplementedError("Livello non presente!")
    game = _3inarow((dim,dim))
    gui_play(game)
main()


'''
                if (a*rig+b)//rig == (a*rig+b-1)//rig == (a*rig+b-2)//rig:
                    #controllo righe
                    #caso w w - || b b -
                    if (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "B" 
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "w"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "B" 
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "W" 
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "b"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "W" 
                    elif (m[a * cln + (b-1)] == "W" and m[a * cln + (b-2)] == "w"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "B" 
                    elif (m[a * cln + (b-1)] == "w" and m[a * cln + (b-2)] == "W"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "B"
                    elif (m[a * cln + (b-1)] == "B" and m[a * cln + (b-2)] == "b"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "W" 
                    elif (m[a * cln + (b-1)] == "b" and m[a * cln + (b-2)] == "B"):
                        if m[a * cln + b] == "-": m[a * cln + b] = "W" 
                    #controllo colonne
                    #caso w w - || b b -
                    if (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "B"  
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "w"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "B" 
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "W" 
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "b"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "W" 
                    elif (m[(b-1) * cln + a] == "W" and m[(b-2) * cln + a] == "w"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "B" 
                    elif (m[(b-1) * cln + a] == "w" and m[(b-2) * cln + a] == "W"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "B" 
                    elif (m[(b-1) * cln + a] == "B" and m[(b-2) * cln + a] == "b"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "W" 
                    elif (m[(b-1) * cln + a] == "b" and m[(b-2) * cln + a] == "B"):
                        if m[b * cln + a] == "-": m[b * cln + a] = "W" 
                    #controllo righe
                    #caso - b b || - w w
                    if (m[a * cln + b] == m[a * cln + (b-1)] == "W"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "B" 
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "w"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "B" 
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "B"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "W" 
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "b"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "W" 
                    elif (m[a * cln + b] == "W" and m[a * cln + (b-1)] == "w"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "B" 
                    elif (m[a * cln + b] == "w" and m[a * cln + (b-1)] == "W"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "B" 
                    elif (m[a * cln + b] == "B" and m[a * cln + (b-1)] == "b"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "W" 
                    elif (m[a * cln + b] == "b" and m[a * cln + (b-1)] == "B"):
                        if m[a * cln + (b-2)] == "-": m[a * cln + (b-2)] = "W"  
                    # controllo colonne
                    #caso - w w || - b b
                    if (m[b * cln + a] == m[(b-1) * cln + a] == "W"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "B" 
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "w"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "B" 
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "B"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "W" 
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "b"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "W" 
                    elif (m[b * cln + a] == "W" and m[(b-1) * cln + a] == "w"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "B" 
                    elif (m[b * cln + a] == "w" and m[(b-1) * cln + a] == "W"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "B" 
                    elif (m[b * cln + a] == "B" and m[(b-1) * cln + a] == "b"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "W" 
                    elif (m[b * cln + a] == "b" and m[(b-1) * cln + a] == "B"):
                        if m[(b-2) * cln + a] == "-": m[(b-2) * cln + a] = "W" 
                    # controllo righe
                    # caso w - w || b - b
                    if (m[a * cln + b] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "B" 
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "w"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "B"
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "W" 
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "b"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "W" 
                    elif (m[a * cln + b] == "W" and m[a * cln + (b-2)] == "w"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "B" 
                    elif (m[a * cln + b] == "w" and m[a * cln + (b-2)] == "W"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "B"                     
                    elif (m[a * cln + b] == "B" and m[a * cln + (b-2)] == "b"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "W" 
                    elif (m[a * cln + b] == "b" and m[a * cln + (b-2)] == "B"):
                        if m[a * cln + (b-1)] == "-": m[a * cln + (b-1)] = "W" 
                    #controllo colonne                      
                    # caso w - w || b - b
                    if (m[b * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "B"  
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "w"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "B" 
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "W" 
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "b"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "W" 
                    elif (m[b * cln + a] == "W" and m[(b-2) * cln + a] == "w"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "B" 
                    elif (m[b * cln + a] == "w" and m[(b-2) * cln + a] == "W"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "B"                     
                    elif (m[b * cln + a] == "B" and m[(b-2) * cln + a] == "b"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "W" 
                    elif (m[b * cln + a] == "b" and m[(b-2) * cln + a] == "B"):
                        if m[(b-1) * cln + a] == "-": m[(b-1) * cln + a] = "W"
'''