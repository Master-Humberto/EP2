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
## Funções 
from lista_de_paises import * 
import random
def pais_escolhido():
    return random.choice(lista_paises())
## Base de paises
pais = pais_escolhido()
tentativas = 20
print(pais) # retirar isso depois
print(f"Suas dicas são: {tentativas}")
l= []
while tentativas != 0 :
    pergunta = input("Qual seu paplite?")
    if pergunta == "dica":
        print(mercado_de_dicas(pais,tentativas))
    if pergunta == pais:
        print("Você acertou!")
        tentativas = 0
    elif pergunta in lista_paises():
        tentativas -= 1 
        l = adiciona_em_ordem(pergunta, distancia(pais, pergunta), l)   
        print(l)
    elif pergunta == "desisto":
        print("Ok")
        tentativas= 0
    elif pergunta == "inventario":
        pass
    elif pergunta not in lista_paises():
        print("Por favor, insira um país válido")
    print(f"Suas tentativas são: {tentativas}")










