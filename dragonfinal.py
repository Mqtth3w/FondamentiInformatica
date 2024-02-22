from actor import Actor, Arena
from random import randint
import g2d

Gravity = 0.4
VITEVERDE, SPEEDVERDE = 3, 4
VITEBLU, SPEEDBLU = 3, 4

SPEEDBUBBLE = 6
SPEEDBLUBBA = 4
SPEEDSTONER = 4

class Baron_von_blubba(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._speed = SPEEDBLUBBA
        self._arena_w, self._arena_h = self._arena.size()
        self._o, self._k = 0, 330
        self._landed = False
        self._lives = 1
        self._arena.add(self)

    def move(self):
        self._dy += Gravity
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
           
    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        if isinstance(other, DragonGreen):
            other.death()
         
        if isinstance(other, DragonBlue):
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
           
    def death(self):
        self._lives -= 1
        if self._lives == 0:
            self._arena.remove(self)

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 0, 330
        elif self._dx > 0:
            self._o, self._k = 1266, 330
        return self._o, self._k, self._w, self._h
   
class Stoner(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 18, 18
        self._speed = SPEEDSTONER
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._o, self._k = 236, 276
        self._arena_w, self._arena_h = self._arena.size()
        self._landed = False
        self._lives = 1
        self._arena.add(self)
       
    def move(self):
        self._dy += Gravity
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
           
    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        if isinstance(other, DragonGreen):
            other.death()
           
        if isinstance(other, DragonBlue):
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
            self._dy, self._landed = -9, False
           
    def death(self):
        self._lives -= 1
        if self._lives == 0:
            self._arena.remove(self)
           
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 236, 276
        elif self._dx > 0:
            self._o, self._k = 1034, 276
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
   
    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
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
        self._o, self._k = 575, 330
        self._arena.add(self)
        self._bubgreen, self._bubblue = 0, 0
       
    def move(self):
        self._y += self._dy
        if self._y < 0:
            self._arena.remove(self)
       
        self._x += self._dx
        if self._x < 0:
            self._arena.remove(self)
             
        if abs(self._x - self._lastx) > 60:
            self._y -= 3
            self._dx = 0
 
    def collide(self, other):
        if isinstance(other, DragonGreen):
            self._bubgreen+=1
            if self._bubgreen > 7:
                self._o, self._k = 590, 330
               
        if isinstance(other, DragonBlue):
            self._bubblue+=1
            if self._bubblue > 7:
                self._o, self._k = 590, 330
               
        if isinstance(other, Stoner):
            if self._o == 575 and self._k == 330:
                self._o, self._k = 185, 1070
                other.death()
               
        if isinstance(other, Baron_von_blubba):
            if self._o == 575 and self._k == 330:
                self._o, self._k = 932, 328
                other.death()
               
    def go_left(self):
        self._dx = -self._speed
       
    def go_right(self):
        self._dx = +self._speed
           
    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        if self._o == 590 and self._k == 330:
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
        self._o, self._k = 0, 12
       
    def move(self):
        self._dy += Gravity
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
           
    def add_bubble(self, arena):
        if self._lives > 0:
            if self._o  == 0:
                b = Bubble(arena, self._x, self._y)
                b.go_left()
            if self._o == 942:
                b = Bubble(arena, self._x, self._y)
                b.go_right()


    def lives(self) -> int:
        return self._lives
   
    def collide(self, other):
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

    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 0, 12
        elif self._dx > 0:
            self._o, self._k = 942, 12
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
        self._o, self._k = 0, 12
       
    def move(self):
        self._dy += Gravity
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
           
    def add_bubble(self, arena):
        if self._lives > 0:
            if self._o  == 0:
                b = Bubble(arena, self._x, self._y)
                b.go_left()
            if self._o == 942:
                b = Bubble(arena, self._x, self._y)
                b.go_right()


    def lives(self) -> int:
        return self._lives
   
    def collide(self, other):
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

    def position(self):
        return self._x, self._y, self._w, self._h
   
    def symbol(self):
        if self._dx < 0:
            self._o, self._k = 0, 12
        elif self._dx > 0:
            self._o, self._k = 942, 12
        return self._o, self._k, self._w, self._h
       
       
class BubbleBobbleGame:
    def __init__(self):
        self._arena = Arena((512, 424))
       
        Platform(self._arena, (0, 0), (32, 424)) #paretesinistra
        Platform(self._arena, (480, 0), (32, 424)) #paretedestra
        Platform(self._arena, (32, 0), (452, 32)) #soffitto
        Platform(self._arena, (32, 400), (452, 32)) #pianoterra
        Platform(self._arena, (110, 320), (290, 18)) #primopiano
        Platform(self._arena, (32, 320), (32, 18))
        Platform(self._arena, (448, 320), (32, 18))
        Platform(self._arena, (110, 240), (290, 18)) #secondopiano
        Platform(self._arena, (32, 240), (32, 18))
        Platform(self._arena, (448, 240), (32, 18))
        Platform(self._arena, (110, 160), (290, 18)) #terzopiano
        Platform(self._arena, (32, 160), (32, 18))
        Platform(self._arena, (448, 160), (32, 18))

        self._stoner = Stoner(self._arena, (50, 280))
        self._vonblubba = Baron_von_blubba(self._arena, (50, 80))
        self._dragongreen = DragonGreen(self._arena, (350, 350))
        self._dragonblue = DragonBlue(self._arena, (355, 355))

    def arena(self) -> Arena:
        return self._arena

    def dragongreen(self) -> DragonGreen:
        return self._dragongreen
   
    def dragonblue(self) -> DragonBlue:
        return self._dragonblue
   
    def stoner(self) -> Stoner:
        return self._stoner
   
    def vonblubba(self) -> Baron_von_blubba:
        return self._vonblubba

    def game_over(self) -> bool:
        return self._dragongreen.lives() <= 0 and self._dragonblue.lives() <= 0

    def game_won(self) -> bool:
        return self._vonblubba.lives() <= 0 and self._stoner.lives() <= 0

       
class BubbleBobbleGui:
    def __init__(self):
        self._game = BubbleBobbleGame()
        g2d.init_canvas(self._game.arena().size())
        self._skins = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")
        self._platforms = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble-tiles.png")
        self._maps = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble-maps.png")
        g2d.main_loop(self.tick)
       
    def handle_keyboard(self):
        dragong = self._game.dragongreen()
       
        dragonb = self._game.dragonblue()
       
        if g2d.key_pressed("ArrowUp"):
            dragonb.go_up()
        if g2d.key_pressed("ArrowRight"):
            dragonb.go_right(True)
        elif g2d.key_released("ArrowRight"):
            dragonb.go_right(False)
        if g2d.key_pressed("ArrowLeft"):
            dragonb.go_left(True)
        elif g2d.key_released("ArrowLeft"):
            dragonb.go_left(False)
        if g2d.key_pressed("Spacebar"):
            dragonb.add_bubble(self._game.arena())
        if g2d.key_pressed("w"): #ArrowUp
            dragong.go_up()
        if g2d.key_pressed("d"): #ArrowRight
            dragong.go_right(True)
        elif g2d.key_released("d"):
            dragong.go_right(False)
        if g2d.key_pressed("a"): #ArrowLeft
            dragong.go_left(True)
        elif g2d.key_released("a"):
            dragong.go_left(False)
        if g2d.key_pressed("c"):
            dragong.add_bubble(self._game.arena())
       
    def tick(self):
        self.handle_keyboard()
        arena = self._game.arena()
        arena.move_all()
           
        g2d.clear_canvas()
        g2d.draw_image(self._maps,((0,0),(0,0))) #liv 1
        for a in arena.actors():
            if a.symbol() != (0, 0, 0, 0):
                g2d.draw_image_clip(self._skins, a.symbol(), a.position())

        viteverde = "Vite Verde: " + str(self._game.dragongreen().lives())
        viteblu = "Vite Blu: " + str(self._game.dragonblue().lives())
        g2d.set_color((200,0,0))
        g2d.draw_text(viteverde + " " + viteblu, (130, 34), 34)
           
        if self._game.game_over():
            g2d.alert("GAME OVER")
            g2d.close_canvas()
        elif self._game.game_won():
            g2d.alert("GAME WON")
            g2d.close_canvas()

gui = BubbleBobbleGui()