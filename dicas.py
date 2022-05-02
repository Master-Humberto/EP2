
from sorteando_letra_com_restricoes import *
from sorteando_paises import *
from base_de_paises_normalizada import * 
from lista_de_paises import * 
from capital import *
import random 
from cores_da_bandeira import *


def mercado_de_dicas(pais, tentativas):
    print("Mercado de dicas")
    print("------------------------------------------")
    print('1. Cor da bandeira   - custa 4 tentativas')
    print("2. Letra da capital - custa 3 tentativas")
    print("3. Área              - custa 6 tentativas")
    print("4. População         - custa 5 tentativas")
    print("5. Continente        - custa 7 tentativas")
    print("0. Sem dica")
    print("-----------------------------------------")
    print("Escolha sua opção: [0][1][2][3][4][5]")
    dica = int(input("Qual a sua dica?"))
    if dica == 1:
        tentativas -=4
        return color(pais)
    if dica == 2:
        tentativas -= 3
        return sorteia_letra(capital(pais))
    if dica == 3:
        pass
    if dica == 4:
        pass
    if dica == 5:
        pass
    if dica == 0:
        pass
    
