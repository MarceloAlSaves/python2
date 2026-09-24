print("Jokenpo: Pedra, Papel e Tesoura")
print("Escolha uma das opções abaixo:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
jogador = int(input("Digite a opção desejada: "))
import random
computador = random.randint(1, 3)
if jogador == 1:
    if computador == 1:
        print("Empate! Ambos escolheram Pedra.")
    elif computador == 2:
        print("Você perdeu! O computador escolheu Papel.")
    else:
        print("Você ganhou! O computador escolheu Tesoura.")
elif jogador == 2:
    if computador == 1:
        print("Você ganhou! O computador escolheu Pedra.")
    elif computador == 2:
        print("Empate! Ambos escolheram Papel.")
    else:
        print("Você perdeu! O computador escolheu Tesoura.")
elif jogador == 3:
    if computador == 1:
        print("Você perdeu! O computador escolheu Pedra.")
    elif computador == 2:
        print("Você ganhou! O computador escolheu Papel.")
    else:
        print("Empate! Ambos escolheram Tesoura.")
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")
