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
from termcolor import colored, cprint # 15
from nada import * # 16
from colorama import Fore, Back, Style # 17
def pais_escolhido():
    return random.choice(lista_paises())
## Base de paises
pais = pais_escolhido()
tentativas = 20
print(f"Suas dicas são: {tentativas}")
l= []
cores = []
dinkins = []
jogar_novamente = 1
print(pais) # tirar isso depois
while jogar_novamente != 0:
    if tentativas <= 0 :
        jogar_novamente = input("Quer jogar novamente [s|n]")
        if jogar_novamente == 's':
            tentativas = 20
            pais = pais_escolhido()
        else:
            break
    pergunta = input("Qual seu paplite?")
    if pergunta == "dica":
        dica, tentativas = mercado_de_dicas(pais,tentativas,cores)
        dinkins.append(dica)
        print(f"Distâncias:{l}")
        if nada() in dinkins:
            dinkins.remove(nada())
        print(f"Dicas : {dinkins}")
    if pergunta == pais:
        print("Você acertou!")
        tentativas = 0
    if pergunta not in lista_paises():
        print("Insira um país válido")
    if pergunta == "desisto":
        break
    if pergunta == "inventario":
        print(f"Distâncias:{l}")
        if nada() in dinkins:
            dinkins.remove(nada())
        print(f"Dicas : {dinkins}")
    
    if nada() in dinkins:
        dinkins.remove(f"{nada()}")
        print(l) 
    if pergunta in lista_paises():
        dinkins.append(dica)
        print(f"Distâncias:{l}")
        if nada() in dinkins:
            dinkins.remove(nada())
        print(f"Dicas : {dinkins}")

print("Até a próxima!")









