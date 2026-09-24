print("Confederação Nacional de Natação")
idade = int(input("Digite a idade do atleta: "))
if idade <= 9:
    print("Categoria: Mirim")
elif idade <= 14:
    print("Categoria: Infantil")
elif idade <= 19:
    print("Categoria: Júnior")
elif idade <= 25:
    print("Categoria: Sênior")
else:
    print("Categoria: Master")