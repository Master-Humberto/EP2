import random

def sorteia_letra(s,l):
    print(s) 
    pop = ""
    lista_simbolos = ['.', ',', '-', ';', ' ']
    for i in range(0, len(lista_simbolos)):
        l.append(lista_simbolos[i])
    for i in range(0, len(s)):
        if s[i].lower() not in l:
            pop += s[i].lower()
    if len(pop) == 0: 
        return ""
    print(pop)
    k = random.choice(list(pop))
    return k 