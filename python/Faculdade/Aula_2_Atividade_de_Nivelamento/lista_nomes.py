nomes = ["Gustavo", "Bruno", "Sara", "João", "Thaina"]
# exiba todos os nomes OK
for nome in nomes:
    print(nome)

# conte quantos foram cadastrados OK
print("\nForam cadastrados " + str(len(nomes)))

# permita pesquisar se um nome específico está na lista OK
while True:
    nome_solicitado = input("\nDigite qual nome gostaria de procurar na lista" +
                            "(Caso queira parar a busca, insira 'q') ")
    if nome_solicitado == "q":
        break
    elif nome_solicitado.title() in nomes:
        print("O nome pesquisado está na lista!")
    else:
        print("O nome solicitado não está na lista.")