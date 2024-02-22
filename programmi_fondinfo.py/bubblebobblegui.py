from bubblebobblegame import BubbleBobbleGame
import g2d
      
LIV = 1
class BubbleBobbleGui:
    def __init__(self):
        self._name_g = str(input("Name player green? "))
        self._name_b = str(input("Name player blue? "))
        self._game = BubbleBobbleGame((LIV))
        g2d.init_canvas(self._game.arena().size())
        self._skins = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")
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
        if g2d.key_pressed("w"): 
            dragong.go_up()
        if g2d.key_pressed("d"):
            dragong.go_right(True)
        elif g2d.key_released("d"):
            dragong.go_right(False)
        if g2d.key_pressed("a"): 
            dragong.go_left(True)
        elif g2d.key_released("a"):
            dragong.go_left(False)
        if g2d.key_pressed("s"):
            dragong.add_bubble(self._game.arena())
       
    def tick(self):
        global LIV
        self.handle_keyboard()
        arena = self._game.arena()
        arena.move_all()
        g2d.clear_canvas()
        
        if LIV == 1:
            g2d.draw_image(self._maps,((0,0),(0,0))) 
        elif LIV == 2:
            g2d.draw_image_clip(self._maps, (512,0,512,424), (0,0,512,424)) 
            
        for a in arena.actors():
            if a.symbol() != (0, 0, 0, 0):
                g2d.draw_image_clip(self._skins, a.symbol(), a.position())

        green_game = f"{self._name_g} ♥: "+str(self._game.dragongreen().lives())+"   "+"points: "+str(self._game.dragongreen().points())
        blue_game = f"{self._name_b} ♥: "+str(self._game.dragonblue().lives())+"   "+"points: "+str(self._game.dragonblue().points())
        g2d.set_color((0,255,0))
        g2d.draw_text(green_game, (35, 34), 14)
        g2d.set_color((0,255,255))
        g2d.draw_text(blue_game, (35, 50), 14)
           
        if self._game.game_over():
            g2d.alert("GAME OVER")
            g2d.close_canvas()
            
        if LIV == 1 and self._game.game_won():
            LIV += 1
            g2d.alert("Start level 2")
            self._game = BubbleBobbleGame((LIV))
        elif LIV == 2 and self._game.game_won():
            g2d.alert("GAME WON")
            g2d.close_canvas()

gui = BubbleBobbleGui()
