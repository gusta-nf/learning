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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialization with atributtes '''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Cream', 'Chocolate', 'Strawberry', 'Vanilla']

    def introducing_flavors(self):
        '''Showing flavor options'''
        print("This is options of ice cream avaiable: " + str(self.flavors))

# 9.6 Exercise
ice_cream = IceCreamStand("Ravi's", "Ice Cream")
ice_cream.introducing_flavors()