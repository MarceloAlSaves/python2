print("Escolha uma das opções abaixo para conversão:")
print("1 - Para binário")
print("2 - Para octal")
print("3 - Para hexadecimal")
pergunta1 = float(input("Digite a opção desejada: "))
if pergunta1 == 1:
    numero = int(input("Digite um número inteiro: "))
    print("O número {} em binário é {}".format(numero, bin(numero)[2:]))
elif pergunta1 == 2:
    numero = int(input("Digite um número inteiro: "))
    print("O número {} em octal é {}".format(numero, oct(numero)[2:]))
elif pergunta1 == 3:
    numero = int(input("Digite um número inteiro: "))
    print("O número {} em hexadecimal é {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")