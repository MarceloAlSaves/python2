from random import randint

while True:
    computador = randint(1, 10)
    jogador = int(input("Digite um número de 1 a 10: "))
    escolha = input("Par ou Ímpar? [P/I]: ").upper()
    total = computador + jogador
    print(f"Computador jogou {computador}")
    print(f"Total: {total}")
    if total % 2 == 0:
        resultado = "P"
        print("Deu PAR!")
    else:
        resultado = "I"
        print("Deu ÍMPAR!")
    if escolha == resultado:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    continuar = input("Quer jogar novamente? [S/N]: ").upper()
    if continuar == "N":
        break
print("Fim de jogo!")
