print("Cadastro de 4 pessoas")

soma = 0
homem_velho = "Nenhum"
idade_velho = 0
mulheres = 0

for i in range(1, 5):
    nome = input(f"Nome da pessoa {i}: ").strip()
    idade = int(input(f"Idade da pessoa {i}: "))
    sexo = input(f"Sexo [M/F]: ").strip().upper()

    soma += idade

    if sexo == "M" and idade > idade_velho:
        idade_velho = idade
        homem_velho = nome
    elif sexo == "F" and idade < 20:
        mulheres += 1

print(f"\nMédia de idade: {soma / 4:.2f}")
print(f"Homem mais velho: {homem_velho}")
print(f"Mulheres menores de 20 anos: {mulheres}")