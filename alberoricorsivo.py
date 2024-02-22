
import g2d
import math

def move_pen(pos: (float, float), tronco: float, angolo: float) -> (float, float):
    x, y = pos
    x1 = x + math.cos(angolo) * tronco
    y1 = y + math.sin(angolo) * tronco
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

def albero(pos: (float, float), tronco: float, angolo: float):
    if tronco < 5:
        g2d.set_color((0,255,0))
        move_pen(pos, tronco, angolo)
    else:
        g2d.set_color((30,30,0))
        albero(move_pen(pos, tronco, angolo), tronco*4/5, angolo - math.pi/6)
        g2d.set_color((30,30,0))
        albero(move_pen(pos, tronco, angolo), tronco*4/5, angolo + math.pi/6)
        
def main():
    g2d.init_canvas((1100, 650))
    albero((550, 650), 125, -math.pi/2)
    g2d.main_loop()
main()
    