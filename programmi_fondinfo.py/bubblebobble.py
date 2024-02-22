from actor import Actor
from random import randint
from time import time
#gravitazione
GRAVITY = 0.4
#nemico blubba
SPEEDBLUBBA, SALTOBLUBBA, BLUBBAIMGSX, BLUBBAIMGDX  = 4, -8, (0, 330), (1266, 330)
#nemico stoner
SPEEDSTONER, SALTOSTONER, STONERIMGSX, STONERIMGDX  = 4, -8, (236, 276), (1034, 276)
#velocità bolla, distanza limite per cui inizia a salire
SPEEDBUBBLE, BUBBLELIMIT, BUBBLEVELOCITASALITA = 6, 60, 2 
BUBBLEIMG, BUBBLEEXPLODE = (575, 330), (590, 330)
BUBBLESTONER, BUBBLEBLUBBA = (185, 1070), (932, 328)
#drago verde
VITEVERDE, SPEEDVERDE, SALTOVERDE = 3, 4, -8.15
VERDEIMGSX, VERDEIMGDX = (0, 12), (1266, 12)
#drago blu
VITEBLU, SPEEDBLU, SALTOBLU = 3, 4, -8.15
BLUIMGSX, BLUIMGDX = (326, 12), (942, 12)


class Baron_von_blubba(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._speed = SPEEDBLUBBA
        self._arena_w, self._arena_h = self._arena.size()
        self._o, self._k = BLUBBAIMGSX
        self._landed = False
        self._arena.add(self)

    def move(self):
        self._dy += GRAVITY
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > self._arena_h - self._h:
            self._y = self._arena_h - self._h
            self._landed = True
           
        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w
           
        mblubba = randint(50,70)
        if mblubba == 50:
            nvb = randint(4,6)
            if nvb == 4:
                self.go_left()
            elif nvb == 5:
                self.go_right()
            elif nvb == 6:
                self.go_up()

    def collide(self, other):
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  
            x2, y2, w2, h2 = other.position()
           
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
           
            nearb = min(borders)  
           
            self._y += nearb[2] * nearb[0]  
            self._x += nearb[1] * nearb[0]  
               
            if nearb[2] < 0:
                self._landed = True
            if nearb[2] != 0:
                self._dy = 1
               
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed

    def go_up(self):
        if self._landed:
            self._dy, self._landed = SALTOBLUBBA, False

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def symbol(self) -> (int, int, int, int):
        if self._dx < 0:
            self._o, self._k = BLUBBAIMGSX
        elif self._dx > 0:
            self._o, self._k = BLUBBAIMGDX
        return self._o, self._k, self._w, self._h
   
class Stoner(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._speed = SPEEDSTONER
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._o, self._k = STONERIMGSX
        self._arena_w, self._arena_h = self._arena.size()
        self._landed = False
        self._arena.add(self)
       
    def move(self):
        self._dy += GRAVITY
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > self._arena_h - self._h:
            self._y = self._arena_h - self._h
            self._landed = True
           
        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w
              
        mstoner = randint(0,20)
        if mstoner == 0:
            nst = randint(1,3)
            if nst == 1:
                self.go_left()
            elif nst == 2:
                self.go_right()
            elif nst == 3:
                self.go_up()

    def collide(self, other):
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  
            x2, y2, w2, h2 = other.position()
           
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
           
            nearb = min(borders)  
           
            self._y += nearb[2] * nearb[0]  
            self._x += nearb[1] * nearb[0]  
               
            if nearb[2] < 0:
                self._landed = True
            if nearb[2] != 0:
                self._dy = 1
               
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed

    def go_up(self):
        if self._landed:
            self._dy, self._landed = SALTOSTONER, False
           
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def symbol(self) -> (int, int, int, int):
        if self._dx < 0:
            self._o, self._k = STONERIMGSX
        elif self._dx > 0:
            self._o, self._k = STONERIMGDX
        return self._o, self._k, self._w, self._h
   
   
class Platform(Actor):
    def __init__(self, arena, pos, dim):
        self._x, self._y = pos
        self._w, self._h = dim
        self._arena = arena
        self._arena.add(self)
   
    def move(self):
        pass
   
    def collide(self, other):
        pass
   
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h
   
    def symbol(self) -> (int, int, int, int):
        return 0, 0, 0, 0
   
   
class Bubble(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._lastx = x
        self._w, self._h = 18, 18
        self._speed = SPEEDBUBBLE
        self._arena = arena
        self._arena_w, self._arena_h = self._arena.size()
        self._dx, self._dy = 0, 0
        self._o, self._k = BUBBLEIMG
        self._arena.add(self)
        self._bub_green, self._bub_blue = 0, 0
       
    def move(self):
        self._y += self._dy
        if self._y < 0:
            self._arena.remove(self)
       
        self._x += self._dx
        if self._x < 0:
            self._arena.remove(self)
             
        if abs(self._x - self._lastx) > BUBBLELIMIT:
            self._y -= BUBBLEVELOCITASALITA
            self._dx = 0
 
    def collide(self, other):
        if isinstance(other, DragonGreen):
            self._bub_green+=1
            if self._bub_green > 7:
                if ((self._o, self._k) == BUBBLESTONER) or ((self._o, self._k) == BUBBLEBLUBBA):
                    self._o, self._k = BUBBLEEXPLODE
                    other.incpoints()
                else:
                    self._o, self._k = BUBBLEEXPLODE
               
        if isinstance(other, DragonBlue):
            self._bub_blue+=1
            if self._bub_blue > 7:
                if ((self._o, self._k) == BUBBLESTONER) or ((self._o, self._k) == BUBBLEBLUBBA):
                    self._o, self._k = BUBBLEEXPLODE
                    other.incpoints()
                else:
                    self._o, self._k = BUBBLEEXPLODE
               
        if isinstance(other, Stoner):
            if (self._o, self._k) == BUBBLEIMG:
                self._o, self._k = BUBBLESTONER
                self._arena.remove(other)
                
        if isinstance(other, Baron_von_blubba):
            if (self._o, self._k) == BUBBLEIMG:
                self._o, self._k = BUBBLEBLUBBA
                self._arena.remove(other)   
               
    def go_left(self):
        self._dx = -self._speed
       
    def go_right(self):
        self._dx = self._speed
           
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h
   
    def symbol(self) -> (int, int, int, int):
        if (self._o, self._k) == BUBBLEEXPLODE:
            self._arena.remove(self)
        return self._o, self._k, self._w, self._h


class DragonGreen(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._pos = pos
        self._w, self._h = 20, 20
        self._speed = SPEEDBLU
        self._dx, self._dy = 0, 0
        self._lives = VITEVERDE
        self._arena = arena
        self._arena_w, self._arena_h = self._arena.size()
        self._arena.add(self)
        self._landed = False
        self._guarda = False 
        self._points = 0
        self._o, self._k = VERDEIMGSX
       
    def move(self):
        self._dy += GRAVITY
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > self._arena_h + self._h:
            self.death()
           
        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w
           
        if self._dy > 0:
            self._landed = False
        
        if self._dx > 0:
            self._guarda = True
        elif self._dx < 0:
            self._guarda = False

    def go_left(self, go: bool):
        if go:
            self._dx = -self._speed
        elif self._dx < 0:
            self._dx = 0

    def go_right(self, go: bool):
        if go:
            self._dx = self._speed
        elif self._dx > 0:
            self._dx = 0
           
    def go_up(self):
        if self._landed:
            self._dy, self._landed = SALTOVERDE, False
           
    def add_bubble(self, arena):
        if self._lives > 0:
            if self._guarda == False:
                b = Bubble(arena, self._x, self._y)
                b.go_left()
            if self._guarda == True:
                b = Bubble(arena, self._x, self._y)
                b.go_right()
        
    def incpoints(self):
        self._points += 100

    def lives(self) -> int:
        return self._lives
   
    def collide(self, other):
        if isinstance(other, Stoner):
            self.death()
            
        if isinstance(other, Baron_von_blubba):
            self.death()
        
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  
            x2, y2, w2, h2 = other.position()
           
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
           
            nearb = min(borders)  
           
            if self._dy > 0:
                self._y += nearb[2] * nearb[0]  
                self._x += nearb[1] * nearb[0]  
               
                if nearb[2] < 0:
                    self._landed = True
                if nearb[2] != 0:
                    self._dy = 1
            else:
                self._x += nearb[1] * nearb[0]
                

    def death(self):
        self._lives -= 1
        if self._lives <= 0:
            self._arena.remove(self)
        self._x, self._y = self._pos
        return self._x, self._y
    
    def points(self) -> int:
        return self._points

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h
   
    def symbol(self) -> (int, int, int, int):
        if self._dx < 0:
            self._o, self._k = VERDEIMGSX
        elif self._dx > 0:
            self._o, self._k = VERDEIMGDX
        return self._o, self._k, self._w, self._h
       

class DragonBlue(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._pos = pos
        self._w, self._h = 20, 20
        self._speed = SPEEDBLU
        self._dx, self._dy = 0, 0
        self._lives = VITEBLU
        self._arena = arena
        self._arena_w, self._arena_h = self._arena.size()
        self._arena.add(self)
        self._landed = False
        self._guarda = False
        self._points = 0
        self._o, self._k = BLUIMGSX
       
    def move(self):
        self._dy += GRAVITY
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > self._arena_h + self._h:
            self.death()
           
        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena_w - self._w:
            self._x = self._arena_w - self._w
           
        if self._dy > 0:
            self._landed = False
            
        if self._dx > 0:
            self._guarda = True
        elif self._dx < 0:
            self._guarda = False

    def go_left(self, go: bool):
        if go:
            self._dx = -self._speed
        elif self._dx < 0:
            self._dx = 0

    def go_right(self, go: bool):
        if go:
            self._dx = self._speed
        elif self._dx > 0:
            self._dx = 0
           
    def go_up(self):
        if self._landed:
            self._dy, self._landed = SALTOBLU, False
           
    def add_bubble(self, arena):
        if self._lives > 0:
            if self._guarda == False:
                b = Bubble(arena, self._x, self._y)
                b.go_left()
            if self._guarda == True:
                b = Bubble(arena, self._x, self._y)
                b.go_right()
                
    def incpoints(self):
        self._points += 100

    def lives(self) -> int:
        return self._lives
   
    def collide(self, other):
        if isinstance(other, Stoner):
            self.death()
            
        if isinstance(other, Baron_von_blubba):
            self.death()
            
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  
            x2, y2, w2, h2 = other.position()
           
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
           
            nearb = min(borders)  
           
            if self._dy > 0:
                self._y += nearb[2] * nearb[0]  
                self._x += nearb[1] * nearb[0]  
               
                if nearb[2] < 0:
                    self._landed = True
                if nearb[2] != 0:
                    self._dy = 1
            else:
                self._x += nearb[1] * nearb[0]

    def death(self):
        self._lives -= 1
        if self._lives <= 0:
            self._arena.remove(self)
        self._x, self._y = self._pos
        return self._x, self._y
        
    def points(self) -> int:
        return self._points

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h
   
    def symbol(self) -> (int, int, int, int):
        if self._dx < 0:
            self._o, self._k = BLUIMGSX
        elif self._dx > 0:
            self._o, self._k = BLUIMGDX
        return self._o, self._k, self._w, self._h
       