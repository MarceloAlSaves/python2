
maior18 = homens = mulheres20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    if idade > 18:
        maior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break
print(f"Maiores de 18 anos: {maior18}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheres20}")
