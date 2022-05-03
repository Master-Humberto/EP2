from normaliza_paises import * # 1
from sorteando_letra_com_restricoes import * #2 
from dicas import * #3
from adicionando_em_uma_lista_ordenada import * #4
from haversine import * #5
from esta_na_lista import * #6 
from base_de_paises import * #7
from lista_de_paises import * # 8
import random # 9
from lista_de_paises_e_distancias import * # 11
from distancia_do_pais_escolhido import * # 12
from lista_de_paises import * # 13
import random # 14
from termcolor import colored # 15
def lista_bonita(lista):
    
    for i in range(0, len(lista)):
        if lista[i][1] < 1000:
            lista[i][1] =colored(str(lista[i][1]), 'red', attrs=['reverse', 'blink'])
        elif lista[i][1] < 3000:
                lista[i][1] =colored(str(lista[i][1]), 'orange', attrs=['reverse', 'blink'])
        elif lista[i][1] < 5000:
                lista[i][1] =colored(str(lista[i][1]), 'yellow', attrs=['reverse', 'blink'])
        elif lista[i][1] < 7000:
                lista[i][1] =colored(str(lista[i][1]), 'green', attrs=['reverse', 'blink'])
        elif lista[i][1] >= 7000:
                lista[i][1] =colored(str(lista[i][1]), 'blue', attrs=['reverse', 'blink'])
        return lista

