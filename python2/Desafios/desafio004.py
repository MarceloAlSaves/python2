print("Exercito Brasileiro")
idade = int(input("Digite sua idade, Para sabermos se você pode se alistar: "))
if idade < 18:
    print("Você ainda não pode se alistar, aguarde mais {} anos.".format(18 - idade))
elif idade == 18:
    print("Você deve se alistar imediatamente!")
else:
    print("Você já passou do tempo de se alistar, você deveria ter se alistado há {} anos.".format(idade - 18))