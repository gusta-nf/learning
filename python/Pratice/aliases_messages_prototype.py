var = ''
dicio = {}
lista = []
while True:
    print("Configurando")
    apelido = input(
        "Digite qual será o apelido da mensagem:\n"
        )
    lista.append(apelido)
    mensagem = input(
        "Digite qual será a mensagem correspondente ao apelido:\n"
        )
    dicio[apelido] = mensagem
    repetir = input(
        "Deseja adicionar mais algum apelido?(s/n):\n"
        )
    if repetir == "n":
        break
while True:
    var = input(
        "Digite o apelido que deseja que seja mostrado(para sair digite 0):\n"
        )
    if var == "0":
        break
    elif var not in lista:
        print("O valor fornecido não é um apelido válido")
        continue
    else:
        print(dicio[var])