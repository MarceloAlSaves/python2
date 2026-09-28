Numero1 = int(input("Digite o primeiro número: "))
Numero2 = int(input("Digite o segundo número: "))

opcoes = ["1", "2", "3", "4"]

while True:
    print("===== MENU DE OPÇÕES =====")
    print("O que você deseja fazer com os números {} e {}?".format(Numero1, Numero2))
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Maior")
    print("4 - Sair do programa")

    opcao = input("Digite a opção desejada: ")

    while opcao not in opcoes:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        resultado = Numero1 + Numero2
        print("O resultado da soma é:", resultado)

    elif opcao == "2":
        resultado = Numero1 * Numero2
        print("O resultado da multiplicação é:", resultado)

    elif opcao == "3":
        if Numero1 > Numero2:
            print("O maior número é:", Numero1)
        elif Numero2 > Numero1:
            print("O maior número é:", Numero2)
        else:
            print("Os dois números são iguais.")

    elif opcao == "4":
        print("Saindo do programa")
        break