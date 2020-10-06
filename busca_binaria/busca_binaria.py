from random import randint

def busca_binaria(lista_parametro, procurado):
    """
    Método que consiste em pegar o termo médio da lista para comparar com o valor procurado,
    caso os valores não sejam iguais, ele divide a parte da lista que mais se aproxima do valor até que se ache o valor
    ou não.
    """
    encontrou = False
    inicio = 0
    fim = len(lista_parametro) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if procurado == lista_parametro[meio]:
            encontrou = True
            break
        elif procurado < meio:
            fim = meio - 1
        else:
            inicio = meio + 1

    if encontrou is True:
        print("O valor {0} foi encontrado na lista".format(procurado))
        return True
    else:
        print("O valor NÃO está na lista!")
        return False


quantidade = int(input("Digite a quantidade de termos da sua lista----->"))

lista_gerada = []

for i in range (quantidade):
    sair = True
    termo = randint(0, 10)
    while sair:
        if termo in lista_gerada:
            continue
        else:
            lista_gerada.append(termo)
            sair = False

procurar = "sim"

while procurar == "sim":
    numero = int(input("\nDigite o número que deseja procurar na lista-----> "))
    busca_binaria(sorted(lista_gerada), numero)
    procurar = input("Deseja procurar mais algum número?")

exibir = input("\nDeseja ver a lista gerada?")

if exibir == "sim":
    print(lista_gerada)
else:
    print("Ok então, você que sabe!")

print("\nSeu programa terminou!")