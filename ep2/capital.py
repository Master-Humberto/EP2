
from base_de_paises import * 
from base_de_paises_normalizada import * 
from normaliza_paises import * 
def capital(pais):
    base = normaliza(DADOS)
    capital = base[pais]['capital']
    return capital
    

