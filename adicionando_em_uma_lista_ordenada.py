def adiciona_em_ordem(pais,d,l):
    lista_d = []
    for i in range(0, len(l)):
        lista_d.append(l[i][1])
    print(lista_d)
    p = 0
    for i in range(0, len(lista_d)):
        if d > lista_d[i]:
            p += 1
        elif d < lista_d[i]:
            break
    l.insert(p, [pais, d])
    return l 