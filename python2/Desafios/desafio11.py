import random

print("Fale um número entre 1 e 10 que eu vou adivinhar")
numero = int(input("Digite um número: "))

numero_sorteado = random.randint(1, 10)
tentativas = 1
adivinhou = False

while adivinhou == False:
    if numero == numero_sorteado:
        print("Parabéns! Você adivinhou o número que eu estava pensando!")
        adivinhou = True
    else:
        print("Você errou! Eu estava pensando em um número entre 1 e 10,")
        print("mas não era o {}.".format(numero))
        tentativas += 1
        adivinhou = False
        numero = int(input("Digite outro número: "))

print("Fim do jogo! Obrigado por jogar.")
