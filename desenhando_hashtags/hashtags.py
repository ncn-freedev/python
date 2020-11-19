qtde = int(input("Quantas vezes o desenho deve aparecer?"))

matriz_aux = []

contador = 1

for i in range(qtde):
    print(i)
    matriz = []
    for linha in range(contador):
        for coluna in range(contador):
            matriz_aux.append(" ")
        matriz.append(matriz_aux)
        matriz_aux = []
    contador = contador + 2
    pontomedio = i
    cont = 0
    for linha in matriz:
        if cont <= i:
            if pontomedio >= 0:
                linha[pontomedio] = "#"
            if pontomedio < i and pontomedio >= 0:
                linha[-pontomedio - 1] = "#"
            pontomedio -= 1
            cont += 1
        else:
            pontomedio += 2
            linha[pontomedio] = "#"
            if pontomedio < i and pontomedio >= 0:
                linha[-pontomedio - 1] = "#"
            pontomedio -= 1
        elemento = ""
        for c in linha:
            elemento = elemento + c
        print(elemento)
    
        