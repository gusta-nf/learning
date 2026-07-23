rivers = {
    'Amazonas' : 'Brazil',
    'Ebro' : 'Spain',
    'Nilo' : 'Egypt',
}
for river, country in sorted(rivers.items()):
    print('The ' + river + ' river runs for ' + country  + '.')
for river in sorted(rivers.keys()):
    print(river)
for country in sorted(rivers.values()):
    print(country)
# Don't need sorted to solve, but I like order