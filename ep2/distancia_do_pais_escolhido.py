from haversine import * 
from base_de_paises_normalizada import *
from base_de_paises import *
import matplotlib.pyplot as plt
from termcolor import colored, cprint 
def distancia(pais, pergunta):
    f1 = base_normalizada()[pais]['geo']['latitude']
    l1 = base_normalizada()[pais]['geo']['longitude']
    f2 = base_normalizada()[pergunta]['geo']['latitude']
    l2 = base_normalizada()[pergunta]['geo']['longitude']
    d = haversine(EARTH_RADIUS, f1, l1, f2, l2)
    return d

