def normaliza(dic):
    novodic = {}
    for continente, infos in dic.items():
        for tipo, info in infos.items():
            novodic[tipo] = info
            if tipo == "bandeira":
                novodic['continente'] = continente
    return novodic   