from adicionando_cores import * 


def ajeita(l):
    for i in range(0, len(l)):
        if l[i][1] < 2000:
            print(f"{branco(l[i][0])} -> {vermelho(l[i][1])}")
        elif l[i][1] < 4000:
            print(f"{branco(l[i][0])} -> {amarelo(l[i][1])}")
        elif l[i][1] < 6000:
            print(f"{branco(l[i][0])} -> {verde(l[i][1])}")
        else:
            print(f"{branco(l[i][0])} -> {azul(l[i][1])}")
    return ("------------------------------------------")
    