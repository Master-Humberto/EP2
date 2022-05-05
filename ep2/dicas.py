
import telnetlib
from sorteando_letra_com_restricoes import *
from sorteando_paises import *
from base_de_paises_normalizada import * 
from lista_de_paises import * 
from capital import *
import random 
from cores_da_bandeira import *
from area import *
from populacao import *
from continente import * 
from nada import * 
from lista_letras import * 
def mercado_de_dicas(pais, tentativas,cores, dinkins):
    print("Mercado de dicas")
    print("------------------------------------------")
    if tentativas >= 4:
        print('1. Cor da bandeira   - custa 4 tentativas')
    if tentativas >= 3:
        print("2. Letra da capital - custa 3 tentativas")
    if tentativas >= 6:
        print("3. Área              - custa 6 tentativas")
    if tentativas >= 5:
        print("4. População         - custa 5 tentativas")
    if tentativas >= 7:
        print("5. Continente        - custa 7 tentativas")
    print("0. Sem dica")
    print("-----------------------------------------")
    print("Escolha sua opção: [0][1][2][3][4][5]")
    dica = int(input("Qual a sua dica?"))

    if dica == 1:
        tentativas -=4
        return color(pais), tentativas
    if dica == 2:
        tentativas -= 3
        return (f"letra da capital ->{sorteia_letra(capital(pais), lista_letras(dinkins))}"), tentativas
    if dica == 3:
        tentativas -= 6
        return (f"area do pais ->{area(pais)} km2"), tentativas
    if dica == 4:
        tentativas -=5
        return (f"populacao do pais -> {populacao(pais)} pessoas"), tentativas
    if dica == 5:
        tentativas -= 7
        return (f"continente do pais ->{continente(pais)}"), tentativas
    else:
        tentativas -= 0
        return nada(), tentativas

