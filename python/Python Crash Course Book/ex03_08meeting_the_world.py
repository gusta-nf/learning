countries = ['Switzerland', 'China', 'USA', 'Spain', 'Japan']
print(countries) # Normal
print(sorted(countries)) # A-Z order
print(countries) # Normal order yet
print(sorted(countries, reverse=True)) # Z-A order
print(countries) # Normal order yet
countries.reverse() # Changing to reverse order
print(countries)
countries.reverse() # Reversing the reverse lOL
print(countries) # Normal order
countries.sort() # A-Z order permanetly
print(countries)
countries.sort(reverse=True) # Z-A order permanetly now
print(countries)