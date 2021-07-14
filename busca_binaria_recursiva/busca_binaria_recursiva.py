from random import randint

def busca_binaria_recursiva(lista_parametro, procurado, ini, fim, meio):
    """
    Método que consiste em pegar o termo médio da lista para comparar com o valor procurado,
    caso os valores não sejam iguais, ele divide a parte da lista que mais se aproxima do valor até que se ache o valor
    ou não. Executa de mode recursivo.
    """
    print(lista_parametro)
    if ini > fim:
        return ""
    #Parei aqui no dia 10/10/2020
    

quantidade = int(input("Digite a quantidade de termos da sua lista----->"))

lista_gerada = []

for i in range (quantidade):
    sair = True
    termo = randint(0, 100)
    while sair:
        if termo in lista_gerada:
            print(termo)
            continue
        else:
            lista_gerada.append(termo)
            sair = False

procurar = "sim"

while procurar == "sim":
    numero = int(input("\nDigite o número que deseja procurar na lista-----> "))
    print(busca_binaria_recursiva(sorted(lista_gerada), numero))
    procurar = input("Deseja procurar mais algum número?")

exibir = input("\nDeseja ver a lista gerada?")

if exibir == "sim":
    print(lista_gerada)
else:
    print("Ok então, você que sabe!")

print("\nSeu programa terminou!")