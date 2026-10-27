print("Maior e menor da sequência")
for i in range(1, 6):
    numero = int(input("Digite o {}º número: ".format(i)))
    if i == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print("O maior número digitado foi: {}".format(maior))
print("O menor número digitado foi: {}".format(menor))
