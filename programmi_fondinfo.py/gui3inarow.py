import g2d
from boardgame import BoardGame
from time import time

W, H = 40, 40
LONG_PRESS = 0.5

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._downtime = 0
        self.update_buttons()

    def keyboard(self):
        if g2d.key_pressed("r"):
            self._game.reset()
            self.update_buttons()
        if g2d.key_pressed("h"):
            if self._game.suggerimenti():
                g2d.alert("colore opposto")
            else:
                g2d.alert("mossa corretta")
            self.update_buttons()
        if g2d.key_pressed("b"):
            self._game.solve_recursive(0)
            self.update_buttons() 
        if g2d.key_pressed("a"):
            self._game.automatic_color()
            self.update_buttons()
        if g2d.key_pressed("u"):
            if self._game.unsolvable():
                g2d.alert("Con queste mosse no risolverai il gioco!")
            else:
                g2d.alert("Prima riempi tutte le celle!")

    def tick(self):
        self.keyboard()
        if g2d.key_pressed("LeftButton"):
            self._downtime = time()
        elif g2d.key_released("LeftButton"):
            mouse = g2d.mouse_position()
            x, y = mouse[0] // W, mouse[1] // H
            if time() - self._downtime > LONG_PRESS:
                self._game.flag_at(x, y)
            else:
                self._game.play_at(x, y)
        self.update_buttons()
                        
    def update_buttons(self):
        g2d.clear_canvas()
        cols, rows = self._game.cols(), self._game.rows()
        for y in range(rows):
            for x in range(cols):
                value = self._game.value_at(x, y)
                if value == "B":
                    n = (0,0,0)
                elif value == "W":
                    n = (255,255,255)
                elif value == "-":
                    n = (180,180,180)
                elif value == "b":
                    n = (0,0,0)
                elif value == "w":
                    n = (255,255,255)
                g2d.set_color(n)
                g2d.fill_rect((x * H, y * H, W, H))
       
        g2d.set_color((190,130,255))
        for y in range(1, rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        g2d.update_canvas()
               
        g2d.update_canvas()
        #if self._game.finished():
            #g2d.alert(self._game.message())
            #g2d.close_canvas()

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
# -,-,-,-,b,-
# b,w,-,-,-,-
# -,w,-,-,w,-
# -,-,-,-,w,-
# b,-,-,-,-,-
# -,-,w,-,-,w