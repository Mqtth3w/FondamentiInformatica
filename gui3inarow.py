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

    def tick(self):
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
                    n = (170,170,170)
                g2d.set_color(n)
                g2d.fill_rect((x * H, y * H, W, H))
       
        g2d.set_color((180,129,253))
        for y in range(1, rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        g2d.update_canvas()
               
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.close_canvas()

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
   
   