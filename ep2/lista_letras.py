def lista_letras(dica):
    lista = []
    for i in range(0, len(dica)):
        if len(dica[i]) == 1:
            lista.append(dica[i])
    return lista