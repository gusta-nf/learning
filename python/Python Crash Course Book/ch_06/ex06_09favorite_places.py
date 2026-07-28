joao = ['Norway', 'Switzerland']
fernanda = ['Old home', 'Brazil']
rodolfo = ['Italy', 'Amalfi Coast',]
favorite_places = {
    'Rodolfo' : rodolfo,
    'Joao' : joao,
    'Fernanda' : fernanda,
}
for name, place in favorite_places.items():
    print('My friend name is ' + name + " and favorite's place are " + str(place))