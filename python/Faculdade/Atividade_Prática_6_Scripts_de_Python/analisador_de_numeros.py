# Explicando o programa ao usuário
print("\tAnalisador de 10 Números Inteiros(Sem vírgula)\n" +
      "Os 10 números informados terão as seguintes conferências:\n" +
      " Maior número\n Menor número\n Soma dos números\n Média\n" +
      " Quantidade de números pares\n Quantidade de números ímpares")
# Declarando as listas que serão utilizadas
numeros = []
pares = []
# Solicitando o números a serem informados pelo usuário
while len(numeros) != 10:
    num = int(input("Informe um número inteiro " + 
          "para ser adicionado na lista de conferência: "))
    numeros.append(num)
# Conferido o números pares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
# Informando os resultados
print(
    "\nMaior número: " + str(max(numeros)) +
    "\nMenor número: " + str(min(numeros)) +
    "\nSoma dos números: " + str(sum(numeros)) +
    "\nMédia: " + str(sum(numeros)/len(numeros)) +
    "\nQuantidade de números pares: " + str(len(pares)) +
    "\nQuantidade de números ímpares: " + str(len(numeros) - len(pares))
)