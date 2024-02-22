from actor import Actor, Arena
from random import randint
import g2d


class Baron_von_blubba(Actor):
    def __init__(self, arena0, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._dx, self._dy = 0, 0
        self._arena = arena0
        self._speed = 4 
        self._arena_w, self._arena_h = self._arena.size()
        self._o, self._k = 0, 330
        self._landed = False
        arena.add(self)

    def move(self):
        g = 0.4
        self._dy += g
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

    def collide(self, other):
        if isinstance(other, Dragon):
            other.death()
           
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
        self._dx = +self._speed

    def go_up(self):
        if self._landed:
            self._dy, self._landed = -8, False

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 0, 330
        elif self._dx > 0:
            self._o, self._k = 1266, 330
        return self._o, self._k, self._w, self._h
   
   
class Stoner(Actor): 
    def __init__(self, arena0, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._arena = arena0
        self._o, self._k = 236, 276
        self._arena_w, self._arena_h = self._arena.size()
        self._landed = False
        arena.add(self)
       
    def move(self):
        g = 0.4
        self._dy += g
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

    def collide(self, other):
        if isinstance(other, Dragon):
            other.death()
           
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
        self._dx = +self._speed

    def go_up(self):
        if self._landed:
            self._dy, self._landed = -8, False
           
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 236, 276
        elif self._dx > 0:
            self._o, self._k = 1034, 276
        return self._o, self._k, self._w, self._h
   
   
class Platform(Actor):
    def __init__(self, arena0, pos, dim):
        self._x, self._y = pos
        self._w, self._h = dim
        self._arena = arena0
        arena.add(self)
   
    def move(self):
        pass
   
    def collide(self, other):
        pass
   
    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        #g2d.set_color((200,0,0))
        return 0, 0, 0, 0
   
   
class Bubble(Actor):
    def __init__(self, arena0, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._speed = 5
        self._arena = arena0
        self._arena_w, self._arena_h = self._arena.size()
        self._dx, self._dy = 0, 0
        self._o, self._k = 575, 330 
        arena.add(self)
        self._conto = 0
        self._bub = 0
       
    def move(self):
        self._y += self._dy
        if self._y < 0:
            self._arena.remove(self)
        
        self._x += self._dx
        if self._x < 0:
            self._arena.remove(self)
               
        x1, y1, w1, h1 = self.position()  
        x2, y2, w2, h2 = dragon.position()
        frames = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0)]
        frame = min(frames)  # ← →
        
        if self._conto > 15:
            if frame[1] < 0:
                self._y -= 3
                self._dx = 0
            if frame[1] > 0:
                self._y -= 3
                self._dx = 0
        else:
            self._conto+=1
   
    def collide(self, other):
        if isinstance(other, Dragon):
            self._bub+=1
            if self._bub > 7:
                self._o, self._k = 590, 330
                
        if isinstance(other, Stoner):
            if self._o == 575 and self._k == 330:
                self._o, self._k = 185, 1070
                self._arena.remove(other)
           
        if isinstance(other, Baron_von_blubba):
            if self._o == 575 and self._k == 330:
                self._o, self._k = 932, 328
                self._arena.remove(other)
                
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = +self._speed
            
    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        #if self._o == 932 and self._k == 328:
            #self._o, self._k = 932, 328 
        #if self._o == 185 and self._k == 1070:
            #self._o, self._k = 185, 1070
        if self._o == 590 and self._k == 330:
            self._arena.remove(self)
            
        return self._o, self._k, self._w, self._h


class Dragon(Actor):
    def __init__(self, arena0, pos):
        self._x, self._y = pos
        self._b = pos
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._arena = arena0
        self._arena_w, self._arena_h = self._arena.size()
        arena.add(self)
        self._landed = False
        self._o, self._k = 0, 12
       
    def move(self):
        g = 0.4
        self._dy += g
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
            self._dy, self._landed  = -8, False
           
    def add_bubble(self, arena0):
        if self._lives > 0:
            if self._o  == 0:
                b = Bubble(arena0, (self._x-3, self._y))
                b.go_left()
               
            elif self._o == 942:
                b = Bubble(arena0, (self._x+3, self._y))
                b.go_right()


    def lives(self) -> int:
        return self._lives
   
    def collide(self, other):
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  # self's pos
            x2, y2, w2, h2 = other.position() # Platform's pos
           
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
           
            nearb = min(borders)  # find nearest border: ← → ↑ ↓
           
            if self._dy > 0:
                self._y += nearb[2] * nearb[0]  ## sign_dy * distance
                self._x += nearb[1] * nearb[0]  ## sign_dx * distance
               
                if nearb[2] < 0:
                    self._landed = True
                if nearb[2] != 0:
                    self._dy = 1
            else:
                self._x += nearb[1] * nearb[0]

    def death(self):
        self._lives -= 1
        self._x, self._y = self._b
    
        if self._lives == 0:
            self._arena.remove(self)
            g2d.confirm("GAME OVER")
            g2d.close_canvas()

    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        if self._dx < 0: 
            self._o, self._k = 0, 12
        elif self._dx > 0:
            self._o, self._k = 942, 12 
        return self._o, self._k, self._w, self._h
       
       
arena = Arena((512, 424)) #512, 424 dimensioni per le mappe

Platform(arena, (0, 0), (32, 424)) #paretesinistra
Platform(arena, (480, 0), (32, 424)) #paretedestra
Platform(arena, (32, 0), (452, 32)) #soffitto
Platform(arena, (32, 400), (452, 32)) #pianoterra

Platform(arena, (110, 320), (290, 18)) #primopiano
Platform(arena, (32, 320), (32, 18))
Platform(arena, (448, 320), (32, 18))

Platform(arena, (110, 240), (290, 18)) #secondopiano
Platform(arena, (32, 240), (32, 18))
Platform(arena, (448, 240), (32, 18))

Platform(arena, (110, 160), (290, 18)) #terzopiano
Platform(arena, (32, 160), (32, 18))
Platform(arena, (448, 160), (32, 18))

dragon = Dragon(arena, (350, 350))
stoner = Stoner(arena, (50, 280))
vonblubba = Baron_von_blubba(arena, (50, 80))
skins = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")
platforms = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble-tiles.png")
maps = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble-maps.png")


def tick():

    mblubba = randint(50,80)
    if mblubba == 50:
        nvb = randint(4,6)
        if nvb == 4:
            vonblubba.go_left()
        elif nvb == 5:
            vonblubba.go_right()
        elif nvb == 6:
            vonblubba.go_up()
   
    mstoner = randint(0,30)
    if mstoner == 0:
        nst = randint(1,3)
        if nst == 1:
            stoner.go_left()
        elif nst == 2:
            stoner.go_right()
        elif nst == 3:
            stoner.go_up() 

    if g2d.key_pressed("w"): #ArrowUp
        dragon.go_up()
    if g2d.key_pressed("d"): #ArrowRight
        dragon.go_right(True)
    elif g2d.key_released("d"):
        dragon.go_right(False)
    if g2d.key_pressed("a"): #ArrowLeft
        dragon.go_left(True)
    elif g2d.key_released("a"):
        dragon.go_left(False)
       
    if g2d.key_pressed("Spacebar"):
        dragon.add_bubble(arena)
       
    arena.move_all()  
    g2d.clear_canvas()
    g2d.draw_image(maps,((0,0),(0,0))) #map 1
    
    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(skins, a.symbol(), a.position())
        #else:
            #g2d.fill_rect(a.position())
           
def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)
main()