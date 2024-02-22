def max_char(text: str) -> str:
    mas = 0
    if len(text) == 1:
        mas = text
    else:
        first = text[0]
        rest = text[1:]
        mat = max_char(rest)
        mas = max(first , mat) 
    return mas
   
def main():
    text = input("text? ")
    n = max_char(text)
    print("Il carattere massimo è: ", n)
main()