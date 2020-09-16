confirma = False

while confirma is False:
    try:
        termo = int(input("Digite o primeiro termo da PA:\n"))
        razao = int(input("Digite a razão da PA:\n"))
        quantidade = int(input("Digite a quantidade de termos da PA:\n"))
        confirma = True
    except ValueError:
        print("\nVocê deve digitar apenas valores inteiros!\n".upper())


lista_PA = []

contador = 0

while contador < quantidade:
    lista_PA.append(termo)
    termo = termo + razao
    contador += 1

print(lista_PA)