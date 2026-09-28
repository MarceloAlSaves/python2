print("Primo ou não primo")
num = int(input("Digite um número: "))
if num < 2:
    print("O número {} não é primo.".format(num))
else:
    for i in range(2, num):
        if num % i == 0:
            print("O número {} não é primo.".format(num))
            break
    else:
        print("O número {} é primo.".format(num))