print("Calculadora de Notas em Reais(R$2, R$5, R$10, R$20, R$50, R$100)")
while True:
    val = int(input("Insira o valor para calcular quantas notas serão precisas: "))

    trocados = []
    notas = [100, 50, 20, 10, 5, 2]

    if (val % 5 != 0) and (val % 2 != 0):
        print("Não é possível gerar esse troco, "
        "o valor não é divísivel pelas notas disponíveis.")
        break

    for nota in notas:
        a = val // nota
        val = val - (a * nota)
        trocados.append(a)

    for nota in notas:
        b = "Seu troco em notas de R$" + str(nota) + " é: "
        print(b + str(trocados[0]))
        trocados.pop(0)
    break