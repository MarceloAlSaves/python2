print("Validação de dados")
while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo in ["M", "F"]:
        break
    print("Sexo inválido. Digite novamente.")