emprestimo = float(input("Digite o valor das parcelas: "))
if emprestimo > 1000:
    print("Parabéns! Você não pagará juros!")
elif emprestimo > 500 and emprestimo <= 1000:
    print("Juros de 10%")
elif emprestimo > 100 and emprestimo <= 500:
    print("Juros de 20%")
else:
    print("Você não poderá fazer o empréstimo, pois o valor é muito baixo.")
