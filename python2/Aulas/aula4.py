resposta = input("Sim ou não? ")
print(resposta)
while resposta.lower() not in ["sim", "não", "nao"]:
    print("Resposta inválida. Por favor, digite 'Sim' ou 'Não'.")
    resposta = input("Sim ou não? ")
print("Você respondeu:", resposta.format(resposta)
      )
