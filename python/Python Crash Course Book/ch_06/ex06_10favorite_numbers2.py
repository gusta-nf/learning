number_joao_vitor = [7,8]
number_lucas = [7,9]
number_caetano = [25,26]
number_fernanda = [3,4]
number_gustavo = [9,10]
people = {
    'Joao Vitor' : number_joao_vitor,
    'Lucas' : number_lucas,
    'Caetano' : number_caetano,
    'Fernanda' : number_fernanda,
    'Gustavo' : number_gustavo,
}
for person, numbers in people.items():
    print(person + "'s favorite numbers are " + str(numbers))