from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 

def populacao(pais):
    base = normaliza(DADOS)
    pop = base[pais]['populacao']
    return pop