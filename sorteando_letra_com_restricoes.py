import random

def sorteia_letra(s):
    ## LINE BREAKER
    pop = ""    
    lista_simbolos = ['.', ',', '-', ';', ' ']
    for i in range(0, len(s)):
        if s[i].lower() not in lista_simbolos:
            pop += s[i].lower()
    if len(pop) == 0:
        return ""
    p = list(pop)
    k = random.choice(p)
    o = k.lower()
    return o 