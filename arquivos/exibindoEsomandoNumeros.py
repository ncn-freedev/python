'''
Este script lê de um arquivo txt uma série de números inteiros e retorna a soma destes ao final
Ele exibe cada número e sua correspondente posição e a soma de todos eles ao final
O Script será feito utilizando o conceito de file iterator, itterador de arquivo
'''
import time

print("INÍCIO DO PROGRAMA")
time.sleep(1)
print("Lendo arquivo...")
time.sleep(2)

soma = 0
contador = 0

#utilizando o conceito file iterator
for linha in open("inteiros.txt"):#o for roda diretamente na abertura do arquivo, não sendo necessário atribuí-lo à nenhuma variávek
    soma =  soma + int(linha)#executando a soma
    contador += 1#contando a posição da linha lida do arquivo
    print("Posição {0} - Elemento {1}".format(contador, int(linha)))#imprimindo a posição e o elemento lido no arquivo naquela linha

time.sleep(1)

print("\nA soma dos dos elementos é: ", soma)#imprimindo a soma que foi feita a cada leitura de cada linha do arquivo