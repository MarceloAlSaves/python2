
total = produtos1000 = 0
mais_barato = ''
menor_preco = 0
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    total += preco
    if preco > 1000:
        produtos1000 += 1
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        mais_barato = nome
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break
print(f"Total gasto: R$ {total:.2f}")
print(f"Produtos acima de R$1000: {produtos1000}")
print(f"Produto mais barato: {mais_barato}")
