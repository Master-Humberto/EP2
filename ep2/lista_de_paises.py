
from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
def lista_paises():
    base = normalizado(DADOS)
    paises = list(base.keys())
    return paises
