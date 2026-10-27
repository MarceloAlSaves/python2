import random
print("Pedra, papel ou tesoura")
opcoes = ["pedra", "papel", "tesoura"]
escolha_usuario = input("Escolha pedra, papel ou tesoura: ")
escolha_computador = random.choice(opcoes)
if escolha_usuario not in opcoes:
    print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
else:
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_computador)

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")