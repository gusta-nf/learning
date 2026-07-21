print('\t\tConversor de temperaturas')
print('\t===Em  caso  de decimais: Digite os valores com . em vez de ,===')
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius*9/5) + 32
kelvin = celsius + 273
print("A temperatura {}°C equivale a {}°F".format(celsius, fahrenheit))
print("A temperatura {}°C equivale a {}K".format(celsius, kelvin))