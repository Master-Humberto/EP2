from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
import random
def area(pais):
    base = normaliza(DADOS)
    area = base[pais]['area']
    return area
