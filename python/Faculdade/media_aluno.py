'''Calculadora de Média'''
print("\tCalculadora de Aprovação\n")
# Recebendo as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Calculando a Média
media = (nota1 + nota2 + nota3)/3
# Informando a Média
print("A média aritmética das 3 notas do aluno é: " + str(media))
#Conferindo a aprovação
if media < 6:
    print("Infelizmente o aluno foi reprovado.")
else:
    print("Parabéns ao aluno, APROVADO!")