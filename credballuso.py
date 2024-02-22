import g2d
from ColoredBall import ColoredBall, ARENA_W, ARENA_H

def tick():
    g2d.clear_canvas()  # BG
    for b in balls:
        b.move()
        g2d.set_color = (b.color())
        g2d.fill_rect(b.position())  # FG

def main():
    global balls
    balls = [ColoredBall(40, 80), ColoredBall(80, 40), ColoredBall(120, 120)]
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()