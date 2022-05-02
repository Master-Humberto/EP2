from haversine import * 
from base_de_paises_normalizada import *
from base_de_paises import *
def distancia(pais, pergunta):
    f1 = base_normalizada()[pais]['geo']['latitude']
    l1 = base_normalizada()[pais]['geo']['latitude']
    f2 = base_normalizada()[pergunta]['geo']['latitude']
    l2 = base_normalizada()[pergunta]['geo']['latitude']
    d = haversine(EARTH_RADIUS, f1, l1, f2, l2)
    return d 

