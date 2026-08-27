class Restaurant():
    '''Modeling a Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialization with atributtes '''
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        '''Introducing the Restaurant '''
        print("The " + self.name + " is a famous restaurant with " +
        self.cuisine + " style.")

    def open_restaurant(self):
        '''Opening message'''
        print("The " + self.name + " is open!")

# Instancing
restaurant = Restaurant("Brasaria", "Hamburger")

# Atributtes
print(restaurant.name)
print(restaurant.cuisine)

# Methods
restaurant.describe_restaurant()
restaurant.open_restaurant()