import g2d
import math

def move_pen(start: (float, float), length: float, angle: float) -> (float, float):
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

def koch_curve(start: (float, float), length: float, angle: float) -> (float, float):
    if length < 5:
        return move_pen(start, length, angle)
    else:
        part = length/3
        pos = koch_curve(start, part, angle)
        pos = koch_curve(pos, part, angle + -math.pi/3)
        pos = koch_curve(pos, part, angle + math.pi/3)
        pos = koch_curve(pos, part, angle)
        return pos
    
def main():
    g2d.init_canvas((600, 400))
    g2d.set_color((200,200,200))
    koch_curve((0, 300), 600, 0)
    g2d.main_loop()
main()
    
    