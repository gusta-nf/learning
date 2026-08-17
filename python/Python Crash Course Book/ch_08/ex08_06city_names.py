def city_country(city_name, country_name):
    local = city_name + ', ' + country_name
    return local

brazil = city_country('Rio de Janeiro', 'Brazil')
print(brazil)
spain = city_country(city_name = 'Madrid', country_name = 'Spain')
print(spain)
switzerland = city_country('Bern', 'Switzerland')
print(switzerland)