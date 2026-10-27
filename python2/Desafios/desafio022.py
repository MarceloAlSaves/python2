print("Detector de palíndromos")
frase = input("Digite uma frase: ").replace(" ", "").lower()
for i in range(len(frase)):
    if frase[i] != frase[-(i+1)]:
        print("A frase não é um palíndromo.")
        break
else:
    print("A frase é um palíndromo.")
