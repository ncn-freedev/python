'''
Programa para armazenar números reais em um arquivo txt criado na sua execução
'''
print("Início do programa \n\n")

validacao = True #validação para gravar o número digitado no arquivo

arq = open("reais.txt", "w") #abertura do arquivo

#Tratamento de exceção para caso o usuário digite um número real utilizando vírgula, já que o padrão do python é o ponto
try:
    num = float(input("Digite um número real com até 3 casas\n(Utilize . para separar a casa decimal) e caso queira parar digite 0: \n"))
    if validacao == True:
        arq.write("{0:.3f}\n" .format(num))
#caso o primeiro número digitado caia na exceção, a variável num recebe o valor 1 para que seja executado o while sem dar erro e a variável validacao
#recebe o valor False para que esse número não seja gravado no arquivo
except ValueError as Número_com_Vírgula: 
    print("!!O número deve ser digitado com ponto e não com vírgula!!\n")
    num = 1
    validacao = False
    
while num != 0: #while para manter o programa em execução até que o usuário digite 0
    try: #novamente o tratamento de exceção
        num = float(input("Digite um número real com até 3 casas decimais\n(Utilize . para separar a casa decimal) e caso queira parar digite 0: \n"))
        validacao = True
    except ValueError as Número_com_Vírgula:
        print("!!O número deve ser digitado com ponto e não com vírgula!!")
        continue
    if validacao == True and num != 0: #o número será escrito no arquivo caso seja diferente de 0 e caso a variavel validacao seja True
        arq.write("{0:.f}\n" .format(num))

arq.close() #fechamento do arquivo

print("\nFim do Programa.")