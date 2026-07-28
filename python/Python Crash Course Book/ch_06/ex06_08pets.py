chole = {
    'animal_type' : 'Dog',
    'owner' : 'Alfred',
}
newton = {
    'animal_type' : 'Parrot',
    'owner' : 'Aaron',
}
steve = { # Minecraft MENTIONED WOW
    'animal_type' : 'Cat',
    'owner' : 'Alex',
}
pets = [chole, newton, steve]
for pet in pets:
    print('Animal type: ' + pet['animal_type'])
    print('Owner: ' + pet['owner'] + '\n')