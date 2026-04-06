largura = float(input("Qual a largura da parede em metros? "))
altura = float(input("Qual a altura da parede em metros? "))
area = largura * altura
pintando = area/2
print("A área da sua parede equivale a {}m² e serão necessários {}L de tinta.\nTendo em vista que cada 1L de tinta pinta 2m².".format(area, pintando))