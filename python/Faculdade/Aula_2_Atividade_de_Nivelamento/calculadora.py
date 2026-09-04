''' Calculadora de operações básicas'''
print("Calculadora de operações básicas com dois números:\n")

num1 = float(input("Digite o primeiro número da operação: "))
num2 = float(input("Digite o segundo número da operação: "))

# Soma
print("O resultado da soma é: " + str(num1+num2))
# Subtração
print("O resultado da subtração(primeiro - segundo) é: " 
      + str(num1-num2))
print("O resultado da subtração(segundo - primeiro) é: "
      + str(num2-num1))
# Multiplicação
print("O resultado da multiplicação é: " + str(num1*num2))
# Divisão
print("O resultado da divisão(primeiro/segundo) é: " 
      + str(num1/num2))
print("O resultado da divisão(segundo/primeiro) é: " 
      + str(num2/num1))