print("Jogo de adivinhação v2.0")
import random
numero_secreto = random.randint(1, 10)
tentativas = 0
while True:
    palpite = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto em {} tentativas.".format(tentativas))
        break
    else:
        print("Você errou! Tente novamente.")
