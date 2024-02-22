from random import randint

class TargetShooting:
    
    def __init__(self, n):
        self._centers = []
        
        for i in range(n):
            x = randint(0,599)
            y = randint(0,599)
            center = (x,y)
            self._centers.append(center)
        print(self._centers)
    
    def shoot(self, xs, ys) -> bool:
        
        for center in self._centers:
            hit = False
            xc, yc = center
            altox, altoy = xc+25, yc+25
            bassox, bassoy = xc-25, yc-25
            if (bassox <= xc <= altox) and (bassoy <= yc <= altoy):
                hit = True
                return hit
        return hit
    
    
def main():
    n = int(input("Inserire il numero di bersagli "))
    game = TargetShooting(n)
    bers = False
    while bers == False:
        xs = int(input("xs? "))
        ys = int(input("ys? "))
        bers = game.shoot(xs,ys)
        print(bers)
        if bers == True:
            print("You hit the target!")
        else:
            print("Try again!")    
main()