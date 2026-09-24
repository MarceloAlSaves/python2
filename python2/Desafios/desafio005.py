print("Digite sua Nota de 0 a 10 para sabermos se você foi aprovado ou reprovado ou Ate Recuperação: ")
nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Parabéns! Você foi aprovado!")
elif nota >= 5 and nota < 7:
    print("Você está de recuperação!")
else:
    print("Você foi reprovado!")