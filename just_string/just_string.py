palavra = str(input("Digite uma palavra:\n"))
while palavra.isalpha() is False:
    print("\nPor favor, digite apenas letras!\n".upper())
    palavra =str(input("Digite uma palavra:\n"))
else:
    print("\nMuito bem, você digitou apenas letras!")