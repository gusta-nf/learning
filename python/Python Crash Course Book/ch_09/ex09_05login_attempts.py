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
        self.login_attempts = 0
        
    def describe_user(self):
        '''Summary about User.'''
        print("\n-User Summary:\n")
        print("Nickname: " + self.nickname + 
        "\nFirst Name: " + self.first_name +
        "\nLast Name: " + self.last_name +
        "\nContact: " + self.contact + 
        "\nAge: " + str(self.age) + "\n")
        
    def greet_user(self):
        '''Greetings for Users'''
        print("Welcome back " + self.nickname)
        
    def increment_login_attempts(self):
        '''Incrementing login attempts'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        ''' Reseting login attempts'''
        self.login_attempts = 0

# Instantiation
gustavo = User("Gustavo", "Fernandez", "Gusta-nf", "77", 22)

# Methods/User
gustavo.greet_user()
gustavo.describe_user()

gustavo.increment_login_attempts()
print(gustavo.login_attempts)

gustavo.increment_login_attempts()
gustavo.increment_login_attempts()
gustavo.increment_login_attempts()
gustavo.increment_login_attempts()
print(gustavo.login_attempts)
gustavo.reset_login_attempts()
print(gustavo.login_attempts)