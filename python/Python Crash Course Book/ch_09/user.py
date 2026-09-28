class User():
    '''Defining a default User.'''
    
    def __init__(
            self, first_name, last_name, 
            nickname, contact, age):
        '''Initializing the class, with attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.contact = contact
        self.age = age
        
    def describe_user(self):
        '''Resume about User.'''
        print("\n-User Resume:\n")
        print("Nickname: " + self.nickname + 
        "\nFirst Name: " + self.first_name +
        "\nLast Name: " + self.last_name +
        "\nContact: " + self.contact + 
        "\nAge: " + str(self.age) + "\n")
        
    def greet_user(self):
        '''Greetings for Users'''
        print("Welcome back " + self.nickname)