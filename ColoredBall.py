import g2d
from random import randint

ARENA_W, ARENA_H = 480, 360

class ColoredBall:
   
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w = 20
        self._h = 20
        self._dx = 5
        self._dy = 5
        self._a = randint(0, 255)
        self._b = randint(0, 255)
        self._c = randint(0, 255)
        g2d.set_color = (self._a, self._b, self._c) 
        
    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def color(self) -> (int, int, int):
        return self._a, self._b, self._c

#def main():
   
 #   b1 = (50, 100)
  #  b2 = (60, 120)
   # q = ColoredBall(b1, b2)
    #c = q.colorball()
    #print("Il colore è: ", c)
       
#main()  
