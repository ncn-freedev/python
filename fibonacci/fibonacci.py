'''
    Programa que mostra a sequência fibonacci na quantidade escolhida pelo usuário.
'''
quantidade = 0
while quantidade < 2:
    try: #Utilizando try para tratar a exceção caso o usuário digite um dado diferente de um número inteiro
        quantidade = int(input("Quantos números da sequência Fibonacci você quer ver?\n"))
        if quantidade < 2: #verificando se o usuário digitou um número maior que 2, pois os dois primeiros números de fibonacci 
                           #já são por padrão 0 e 1
            print("\nA quantidade digitada deve ser maior que 2\n")
            continue #caso o número digitado seja menor que 2 o programa exibe a msg acima e volta para o início do laço while
    except ValueError:
        print("\nO quantidade digitada deve ser um número inteiro.\n") #mensagem exibida no tratamento da exceção caso o dado 
                                                                       #digitado pelo usuário não seja um número inteiro
    
num1 = 0
num2 = 1
contador = 0
soma = 0
print("{0}, {1}, " .format(num1, num2), end = "") #imprimeindo na tela os dois primeiros números (padrões) da sequência. 
                                                  #Utilizando o end para que não ocorra a quebra de linha na hora da impressão dos dados na tela 

while contador < quantidade - 2: # A quantidade deve ser menos 2 pois 0 e 1 já foram exibidos
    soma = num1 + num2 
    print("{}, " .format(soma), end = "")
    num1 = num2
    num2 = soma
    contador += 1

print("\nFim!")