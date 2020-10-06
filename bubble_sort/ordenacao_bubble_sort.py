from random import randint

quantidade = int(input("Digite qual a quantidade de termos da sua lista!"))

lista_gerada = []

def bubble_sort(lista_parametro):
    mudou = True
    temp = 0
    while mudou is True:
        mudou  = False
        for i in range (len(lista_parametro)-1):
            if lista_parametro[i] > lista_parametro[i+1]:
                temp = lista_parametro[i+1]
                lista_parametro[i+1] = lista_parametro[i]
                lista_parametro[i] = temp
                mudou = True
    return lista_parametro

for i in range (quantidade):
    sair = True
    termo = randint(0, 1000)
    while sair:
        if termo in lista_gerada:
            continue
        else:
            lista_gerada.append(termo)
            sair = False



print(lista_gerada)
print(bubble_sort(lista_gerada))