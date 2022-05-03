
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)
  
def vermelho(string): 
    example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(91) + f"{string}" ## vermelho
    return(example_ansi)
def amarelo(string):
    example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(93) + f"{string}" ## amarelo
    return(example_ansi)
def verde(string):
    example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(92) + f"{string}"  ## verde
    return(example_ansi)
def azul(string):
    example_ansi = ANSI.background(1) + ANSI.color_text(49) + ANSI.style_text(34) + f"{string}"  ## azul
    return(example_ansi)
def branco(string):
    example_ansi = ANSI.background(1) + ANSI.color_text(49) + ANSI.style_text(39) + f"{string}"  ## azul
    return(example_ansi)

def colores(d):
    if d < 2000:
      return vermelho(d)
    elif d < 4000:
        return amarelo(d)
    elif d < 6000:
        return verde(d)
    else:
        return azul(d)