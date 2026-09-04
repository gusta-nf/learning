'''Verificador de Números: Positivos, Negativos ou Zero
Também verificando ímpar e par
'''
print("\tVerificador de números\n" +
      "Verifica: Positivos e Negativos\n" +
      "Verifica: Par ou Ímpar\n" +
      "Verifica: Se ele é zero\n")

num1 = int(input("Escolha um número inteiro e o insira: "))
if num1 == 0:
    print("Seu número é 0")
elif num1 < 0:
    print("Seu número é negativo")
elif num1 > 0:
    print("Seu número é positivo")
if num1//2 != 0:
    print("Seu número é par")
elif num1//2 == 0:
    print("Seu número é ímpar")