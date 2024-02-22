def disposr(n: str) -> str:
    stringa = [(p1+p2+p3)
    
    for p1 in n
        if   'a' <= p1 <= 'z'
            #stringa[str(0)] += p1 
        
        for p2 in n
            if   'a' <= p2 <= 'z'
                #stringa[str(1)] += p2
            
            for p3 in n
                if   'a' <= p3 <= 'z'
                    #stringa[str(2)] += p3
              ]
    return stringa
    
n = disposr("aeiou")
print(n)