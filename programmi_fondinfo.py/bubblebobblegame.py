#from time import time
from bubblebobble import DragonGreen, DragonBlue, Stoner, Baron_von_blubba, Platform
from actor import Arena
       
      
class BubbleBobbleGame:
    def __init__(self, liv):
        self._arena = Arena((512, 424))
        if liv == 1:
            Platform(self._arena, (0, 0), (32, 424)) #paretesinistra
            Platform(self._arena, (480, 0), (32, 424)) #paretedestra
            Platform(self._arena, (32, 0), (452, 32)) #soffitto
            Platform(self._arena, (32, 400), (452, 32)) #pianoterra
            Platform(self._arena, (110, 320), (290, 17)) #primopiano
            Platform(self._arena, (32, 320), (32, 17))
            Platform(self._arena, (448, 320), (32, 17))
            Platform(self._arena, (110, 240), (290, 17)) #secondopiano
            Platform(self._arena, (32, 240), (32, 17))
            Platform(self._arena, (448, 240), (32, 17))
            Platform(self._arena, (110, 160), (290, 17)) #terzopiano
            Platform(self._arena, (32, 160), (32, 17))
            Platform(self._arena, (448, 160), (32, 17))
            self._dragongreen = DragonGreen(self._arena, (256, 380))
            self._dragonblue = DragonBlue(self._arena, (256, 380))
            self._nemici = [Stoner(self._arena, (256, 240)), Baron_von_blubba(self._arena,(256, 240)),
                            Baron_von_blubba(self._arena, (256, 120))]
        elif liv == 2:
            Platform(self._arena, (0, 0), (32, 424)) #paretesinistra
            Platform(self._arena, (480, 0), (32, 424)) #paretedestra
            #Platform(self._arena, (32, 0), (452, 32)) #soffitto
            Platform(self._arena, (32, 400), (452, 32)) #pianoterra
            Platform(self._arena, (64, 320), (112, 17)) #primopiano
            Platform(self._arena, (208, 320), (96, 17)) 
            Platform(self._arena, (336, 320), (112, 17)) 
            Platform(self._arena, (112, 240), (288, 17)) #secondopiano
            Platform(self._arena, (160, 160), (80, 17)) #terzopiano
            Platform(self._arena, (272, 160), (80, 17))
            Platform(self._arena, (208, 80), (96, 17)) #quartopiano
            self._nemici = [Stoner(self._arena, (256, 240)), Stoner(self._arena, (256, 240)),
                            Baron_von_blubba(self._arena,(256, 240)),Baron_von_blubba(self._arena, (256, 120)),
                            Baron_von_blubba(self._arena, (256, 120))]
            self._dragongreen = DragonGreen(self._arena, (256, 380))
            self._dragonblue = DragonBlue(self._arena, (256, 380))


    def arena(self) -> Arena:
        return self._arena

    def dragongreen(self) -> DragonGreen:
        return self._dragongreen
   
    def dragonblue(self) -> DragonBlue:
        return self._dragonblue

    def game_over(self) -> bool:
        return self._dragongreen.lives() <= 0 and self._dragonblue.lives() <= 0

    def game_won(self) -> bool:
        for a in self._nemici:
            if a in self._arena.actors():
                return False
        return True
      