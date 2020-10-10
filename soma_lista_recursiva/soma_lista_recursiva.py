def soma_recursiva(lista):
    """
    Faz a soma de todos os elementos de uma lista. Executa de modo recursivo
    """
    print(lista)
    if lista == []:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(soma_recursiva(lista))