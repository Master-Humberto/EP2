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
from adicionando_cores import * # 18
from printus import * #19
from colore_tentativas import * # 20
from ajeita_distancias import * 
def pais_escolhido():
    return random.choice(lista_paises())
## Base de paises
pais = pais_escolhido()
tentativas = 20
print(f"Suas tentativas são : {branco(tentativas)}")
print("============================")
print("|                            |")
print("| Bem-vindo ao Insper Países |")
print("|                            |")
print(" ==== Design de Software ==== ")
print("")
print("Comandos:")
print("")
print("dica       - entra no mercado de dicas")
print("desisto    - desiste da rodada")
print("inventario - exibe sua posição")
print("Um país foi escolhido, tente adivinhar!")
print("")
l= []
cores = []
dinkins = []
jogar_novamente = 1
while jogar_novamente != 0:
    if tentativas <= 0 :
        print(f"O país era : {pais}")
        jogar_novamente = input(f"Quer jogar novamente {branco('[s|n]')}")
        if jogar_novamente == 's':
            tentativas = 20
            pais = random.choice(lista_paises())
            l = []
            dinkins = []
        else:
            break
    pergunta = input(f"{branco('Qual seu paplite? ')}")
    if pergunta == "dica":
        dica, tentativas = mercado_de_dicas(pais,tentativas,cores, dinkins)
        dinkins.append(dica)
        print(f"{branco(ajeita(l))}")
        if nada() in dinkins:
            dinkins.remove(nada())
        print(f"Dicas : {branco(dinkins)}")
    if pergunta == pais:
        print("Você acertou!")
        tentativas = 0
    if pergunta == "desisto":
        jogar_novamente = input((f"Quer desistir{branco('[s|n]')}?"))
        if jogar_novamente == "s":
            print(f"Que deselegante desistir, o país era : {pais}")
            jogar_novamente = input((f"Quer jogar novamente{branco('[s|n]')}?"))
            if jogar_novamente == "n":
                break
            if jogar_novamente == "s":
                tentativas = 20
                pais = random.choice(lista_paises())
                l = []
                dinkins = []
        else:
            pass
    if pergunta == "inventario":
        print(f"{branco(ajeita(l))}")
        if nada() in dinkins:
            dinkins.remove(nada())
        print(f"Dicas : {branco(dinkins)}")
    if nada() in dinkins:
        dinkins.remove(f"{nada()}")
        print(l) 
    elif pergunta in lista_paises():
        adiciona_em_ordem(pergunta, distancia(pais, pergunta), l)
        if nada() in dinkins:
            dinkins.remove(nada())
        tentativas -=1
        print(f"{branco(ajeita(l))}")
        print(f"Dicas : {branco(dinkins)}")
    elif pergunta not in lista_paises():
        print("Insira um país válido")
    print(f"Suas tenativas são: {colore_tentativas(tentativas)}")
    
print("Até a próxima!")









