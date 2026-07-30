inf_rio = {
    'country' : 'Brazil',
    'population' : '213kk',
    'fact' : 'It was a Brazil capital.',
}
inf_madrid = {
    'country' : 'Spain',
    'population' : '49kk',
    'fact' : ('It is home to Sobrino de Botín, '
    + 'the oldest continuously operating restaurant in the world'),
}
inf_bern = {
    'country' : 'Switzerland',
    'population' : '9kk',
    'fact' : ('Bern is the de facto capital of Switzerland, '
    + 'yet it has no official capital status on paper'),
}
# I prefer to separe because PEP8, with the good pratice of the byte quantify.
cities = {
    'Rio de Janeiro' : inf_rio,
    'Madrid' : inf_madrid,
    'Bern' : inf_bern,
}
for city, info in cities.items():
    print("The " + city + ", that is informations: ")
    print("Country: " + info['country'])
    print("Population: " + info['population'])
    print("Curious fact: " + info['fact'] + "\n")