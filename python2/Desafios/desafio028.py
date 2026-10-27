num = int(input("Digite um número: "))
fat = 1

while num > 1:
    fat *= num
    num -= 1

print(f"Fatorial: {fat}")