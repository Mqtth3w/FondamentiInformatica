def contatesto(t: str) -> (int):
    conto = [0]*10
    
    for i in t:
        if   '0' <= i <= '9':
            conto[int(i)] +=1
        
    return conto

def main():
    text = input("text? ")
    result = contatesto(text)
    print(result)
main()
