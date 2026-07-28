person1 = {
    'first_name' : 'Joao', 
    'last_name' : 'Batista', 
    'age' : 21, 
    'city': 'Angra',
}
person2 = {
    'first_name' : 'Marcelo',
    'last_name' : 'Murta',
    'age' : 21,
    'city' : 'São Paulo',
}
person3 = {
    'first_name' : 'Camila',
    'last_name' : 'Vieira',
    'age' : 20,
    'city' : 'Rio de Janeiro',
}
people = [person1, person2, person3]
for person in people:
    print("Name: " + person['first_name'])
    print("Last name: " + person['last_name'])
    print("Age: " + str(person['age']))
    print("Where?: " + person['city'] + "\n")