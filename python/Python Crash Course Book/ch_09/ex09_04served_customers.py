class Restaurant():
    '''Modeling a Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialization with atributtes '''
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Introducing the Restaurant '''
        print("The " + self.name + " is a famous restaurant with " +
        self.cuisine + " style.")

    def open_restaurant(self):
        '''Opening message'''
        print("The " + self.name + " is open!")
    
    def set_number_served(self, number):
        '''Set the number of served customers'''
        self.number_served = number
    
    def increment_number_served(self, additional):
        '''Increment number of served customers'''
        self.number_served += additional

# Instancing
restaurant = Restaurant("Brasaria", "Hamburger")

# Atributtes
print(restaurant.name)
print(restaurant.cuisine)
print(restaurant.number_served)

# Changing Attributtes 9.4
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.number_served)

# Methods
restaurant.describe_restaurant()
restaurant.open_restaurant()