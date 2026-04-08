'''
Bhaskara
'''
a = int(input("Digite o coeficiente a, aquele que acompanha X²: "))
b = int(input("Digite o coeficiente b, aquele que acompanha o X: "))
c = int(input("Digite o coeficiente independente c, que não é acompanhado por X: "))
x1 = (-b+(((b**2) - 4*a*c)**(1/2)))/(2*a)
x2 = (-b-(((b**2) - 4*a*c)**(1/2)))/(2*a)
print(f"Sua função é {a}x² + {b}x + {c} = 0")
print(f"Os valores de X são exatamente:\nX1= {x1}\nX2= {x2}")