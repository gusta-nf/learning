'''
Que dólar barato nesse exercício!
'''
num = float(input("Quantos reais estão disponíveis?"))
dolar = num/3.27
print("Com R${:.2f} você pode comprar US${:.2f}".format(num, dolar))