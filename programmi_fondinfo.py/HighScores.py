class HighScores:
   
    def __init__(self):
        self._greatest = []
        
    def newscore(self, k: int, q: str):
       
        new = (k,q)
        if self._greatest == []:
            self._greatest.append(new)
        else: 
            n = len(self._greatest)
            for i in range(n):
                elem = self._greatest[i]
                if new >= elem:
                    self._greatest.insert(i,new)
                    break
            if new <= min(self._greatest) and len(self._greatest) < 9:
                self._greatest.append(new)
                
            #if len(self._greatest) > 9:
                #self._greatest.pop(10)
        #print(self._greatest)
   
    def givescore(self):
        return self._greatest
       
   
def main():

    pt = input("Do you want to enter a new score? ")
    vp = input("Do you want to see the best scores? ")
    h = HighScores()
    while pt == 'yes' or vp =='yes':
       
        if pt == 'yes':
            k = int(input("Points? "))
            q = str(input("Name? "))
            h.newscore(k,q)
       
        if vp == 'yes':
            print(h.givescore())
            
        pt = input("Do you want to enter a new score? ")
        vp = input("Do you want to see the best scores? ")
main()