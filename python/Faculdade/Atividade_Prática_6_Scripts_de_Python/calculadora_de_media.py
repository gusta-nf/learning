# Explicando ao usuário
print("\tCalculadora de média e situação do aluno\n" +
      "(Caso tenha números com vírgula use . no lugar da vírgula)")
# Coletando notas, informadas pelo usuário
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
# Calculado Média e Declarando situação vazia
media = (nota1 + nota2 + nota3)/3
situacao = ""
# Verificando a situação
if media < 0:
    print("Um dos valores fornecidos está incorreto")
    situacao = "Inderteminada"
elif media >= 7:
    situacao = "Aprovado"
elif 5 < media < 6.9:
    situacao = "Recuperação"
elif media < 5:
    situacao = "Reprovado"
# Resultado
print("A média do aluno é: " + str(media) +
      ", logo sua situação é " + situacao + ".")