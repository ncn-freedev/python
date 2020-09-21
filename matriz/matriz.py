from random import randint

lin = int(input("Digite o número de linhas da matriz:\n"))
col = int(input("Digite o número de colunas da matriz:\n"))

lista_linha = []
matriz = []

for i in range (lin):
    for j in range (col):
        lista_linha.append(randint(0, 10))
    matriz.append(lista_linha.copy())
    lista_linha.clear()

for linha in matriz:
    print("|", end="")
    for termo in linha:
        print("{:^5d}".format(termo), end="")
    print("|")