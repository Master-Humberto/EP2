##
from adicionando_cores import *


def colore_tentativas(tentativas):
    if tentativas <= 20 and tentativas > 15:
        tentativas = vermelho(tentativas)
        return tentativas
    if tentativas <= 15 and tentativas > 10: 
        tentativas = amarelo(tentativas)
        return tentativas 
    elif tentativas <= 10 and tentativas > 5:
        tentativas = verde(tentativas)
        return tentativas
    else:
        tentativas = azul(tentativas)
        return tentativas  



