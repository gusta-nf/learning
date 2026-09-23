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

class Privileges():
    '''Defining privileges'''
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        '''Showing all privileges from user '''
        print("\nThis is your privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    ''' Creating a Admin User'''
    
    def __init__(self, first_name, last_name, nickname, contact, age):
        '''Initializing the class, with attributes.'''
        super().__init__(first_name, last_name, nickname, contact, age)
        self.privileges = Privileges()
    
# Instances
gustavo = User("Gustavo", "Fernandez", "Gusta-nf", "77", 22)
root = Admin("root", "", "Master", "00", 0)

# Methods/User
gustavo.greet_user()
gustavo.describe_user()

root.greet_user()
root.privileges.show_privileges()