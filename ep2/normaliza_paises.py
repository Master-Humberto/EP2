from base_de_paises import *

def normaliza(dic):
    novodic = {}
    for continente, infos in dic.items():
        for tipo, info in infos.items():
            novodic[tipo] = info
            if tipo == "bandeira":
                novodic['continente'] = continente
    return novodic 
## teste
def normalizado(dic):
    novodic = {}
    for continente, infos in dic.items():
        for tipo, info in infos.items():
            novodic[tipo] = info
            novodic[tipo]['continente'] = continente
    return novodic