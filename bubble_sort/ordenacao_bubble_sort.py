from random import randint

quantidade = int(input("Digite qual a quantidade de termos da sua lista!"))

lista_gerada = []

def bubble_sort(lista_parametro):
    """
    Método de ordenação bubble sort que consiste em comparar dois valores subsequentes de uma lista
    e trocá_los de lugar caso o valor de i+1 seja maior que o valor de i.
    A função executará essas comparações quantas vezes forem necessárias, até que nenhuma troca seja feita.
    """
    mudou = True
    while mudou is True:
        mudou  = False
        for i in range (len(lista_parametro)-1):
            if lista_parametro[i] > lista_parametro[i+1]:
                lista_parametro[i], lista_parametro[i+1] = lista_parametro[i+1], lista_parametro[i]
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