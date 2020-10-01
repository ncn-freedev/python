parar = ""
lista = []

while parar != "s":
    numero = input("Digite um número:\n")
    if numero.isdecimal() is False:
        print("Você deve digitar um número!\n")
        insistiu = False
        while insistiu is False:
            parar = input("Você deseja parar? -> ")
            if parar == "s" or parar == "n":
                insistiu = True
                continue
            else:
                print("Por favor digite s ou n!\n")
                continue
            if parar == "n":
                continue
            elif parar == "s":
                print("")
                break
            
    else:
        lista.append(int(numero))
        insistiu = False
        while insistiu is False:
            parar = input("Você deseja parar? -> ")
            if parar == "s" or parar == "n":
                insistiu = True
            else:
                print("Por favor digite s ou n!\n")
                continue
            if parar == "n":
                continue
            elif parar == "s" :
                print("")
                break
        
if len(lista) == 0:
    print("\nVocê não digitou nenhum número!")
else:
    print("Você digitou {} números. \nA lista é: {}. \nA lista na ordem crescente é: {}. \nA lista ma ordem decrescente é: {}" 
    .format(len(lista), lista, sorted(lista), sorted(lista, reverse=True)))