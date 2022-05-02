from termios import TIOCPKT_DOSTOP
from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
def lista_paises():
    base = normaliza(DADOS)
    paises = list(base.keys())
    return paises

print(lista_paises)