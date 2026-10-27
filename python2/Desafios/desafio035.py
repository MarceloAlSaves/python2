
print("=" * 30)
print("       CAIXA ELETRÔNICO")
print("=" * 30)
valor = int(input("Qual valor deseja sacar? R$ "))
cedulas = 50
total_cedulas = 0
while True:
    if valor >= cedulas:
        valor -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R$ {cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if valor == 0:
            break
print("=" * 30)
print("Saque finalizado! Volte sempre!")
