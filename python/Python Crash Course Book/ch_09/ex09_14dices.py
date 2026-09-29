# Importing randint function from random library
from random import randint

class Die():
    '''Defining a dice'''
    def __init__(self, sides=6):
        '''Initialization for dice class'''
        self.sides = sides
    
    def roll_die(self):
        '''Rolling dice'''
        print(randint(1, self.sides))

# Dices
dice_6 = Die()
dice_10 = Die(10)
dice_20 = Die(20)

# Calling 10 times the dices
for number in range(1, 11):
    print("Rolling a six sides dice: ")
    dice_6.roll_die()
    
for number in range(1, 11):
    print("Rolling a ten sides dice: ")
    dice_10.roll_die()
    
for number in range(1, 11):
    print("Rolling a twenty sides dice: ")
    dice_20.roll_die()