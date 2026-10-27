print("Grupo da Maioridade")
count = 0
count_minor = 0
for i in range(1, 8):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i)))
    if idade >= 18:
        print("Essa pessoa é maior de idade.")
        count += 1
    else:
        print("Essa pessoa é menor de idade.")
        count_minor += 1
print("Quantas pessoas são maiores de idade?")
print(count)
print("Quantas pessoas são menores de idade?")
print(count_minor)
