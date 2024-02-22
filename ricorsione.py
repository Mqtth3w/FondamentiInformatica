import g2d

def sierpinski(liv, x, y, w, h):
    
    w2, h2 = w // 2 , h // 2
    if w2 < 1 or h2 < 1 or liv == 0:
        return
    
    for row in range(2):
        for col in range(2):
                
            x2, y2 = x+col*w2, y+row*h2
            if (col != 0 and row != 1):
                g2d.fill_rect((x2, y2, w2, h2))
            else:
                sierpinski(liv-1, x2, y2, w2, h2)

def main():
    liv = int(input("Scegli il livello di profondità della ricorsione "))
    w, h =  512, 512
    g2d.init_canvas(( w, h))
    g2d.set_color((0,0,0))
    g2d.fill_rect((0, 0, w, h))
    g2d.set_color((255,255,255))
    sierpinski(liv, 0, 0, w, h)
    g2d.main_loop()
main()