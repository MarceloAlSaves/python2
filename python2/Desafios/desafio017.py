print("soma de impares multiplos de 3")
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print("A soma de todos os números ímpares múltiplos de 3 no intervalo de 1 a 500 é:", soma)
