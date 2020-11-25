'''
Este script lê de um arquivo txt uma série de números inteiros e retorna a soma destes ao final
'''
import time #utilizando o método sleep da lib time para dar um intervalo entre a a interação do programa com o usuário

print("INÍCIO DO PROGRAMA\n")
time.sleep(1)#espera de um segundo antes de mostrar a próxima mensagem ao usuário
print("Lendo arquivos\n")
time.sleep(1)
print("Realizando soma\n")
time.sleep(1)

arq = open("inteiros.txt", "r")#abertura do arquivo

linha = arq.readline()# lendo a primeira linha do arquivo

soma = 0

while linha != "":#lendo as linhas até que chegue na última linha que é tem o valor "vazio"
    soma = soma + int(linha)#somando os elementos
    linha = arq.readline()#lendo a próxima linha

arq.close()#fechamento do arquivo

print("Sua soma é {0}".format(soma))#exibindo a soma ao usuário