from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
import random
def color(pais):
    base = normaliza(DADOS)
    cores= base[pais]['bandeira']
    lista_cores = []
    if cores['vermelha'] != 0 :
        lista_cores.append("vermelha")
    if cores['laranja'] != 0 :
        lista_cores.append("laranja")
    if cores['amarela'] != 0 :
        lista_cores.append("amarela")
    if cores['verde'] != 0 :
        lista_cores.append("verde")
    if cores['azul'] != 0 :
        lista_cores.append("azul")
    if cores['azul claro'] != 0 :
        lista_cores.append("azul claro")
    if cores['preta'] != 0 :
        lista_cores.append("preta")
    if cores['branca'] != 0 :
        lista_cores.append("branca")
    return random.choice(lista_cores)
    
print(color('brasil'))