def esta_na_lista(pais, l):
    p = 0
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            if l[i][j] == pais:
                p = 1
    if p == 1 :
        return True
    else:
        return False