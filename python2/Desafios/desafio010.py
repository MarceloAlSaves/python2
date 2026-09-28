print("Teste Palíndromo")
palavra = input("Digite uma palavra: ")
palavra = palavra.replace(" ", "").lower()
if palavra == palavra[::-1]:
    print("A palavra '{}' é um palíndromo.".format(palavra))
else:
    print("A palavra '{}' não é um palíndromo.".format(palavra))