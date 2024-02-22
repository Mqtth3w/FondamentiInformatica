
import math
import g2d

def albero(pos: (float, float), tronco: float, angle: float):
    x, y = pos
    x1 = x + math.cos(angle) * tronco
    y1 = y - math.sin(angle) * tronco
    
    if tronco < 5:
        g2d.set_color((0,255,0))
        g2d.draw_line((x, y), (x1, y1))
    else:
        g2d.set_color((30,30,0))
        g2d.draw_line((x, y), (x1, y1))
        albero((x1, y1), tronco*4/5, angle +math.pi/6)
        albero((x1, y1), tronco*4/5, angle -math.pi/6)
         
    
def main():
    g2d.init_canvas((1000,600))
    albero((500,600),10,math.pi/2)
    g2d.main_loop()
main()