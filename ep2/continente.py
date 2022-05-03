from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
import random
def continente(pais):
    base = normalizado(DADOS)
    continente = base[pais]['continente']

    return continente
