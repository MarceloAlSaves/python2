a, b = 0, 1
cont = int(input("Quantos termos? "))

while cont > 0:
    print(a, end=" ")
    a, b = b, a + b
    cont -= 1