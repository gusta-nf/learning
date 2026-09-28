from user import User
class Admin(User):
    ''' Creating a Admin User'''
    
    def __init__(self, first_name, last_name, nickname, contact, age):
        '''Initializing the class, with attributes.'''
        super().__init__(first_name, last_name, nickname, contact, age)
        self.privileges = Privileges()

class Privileges():
    '''Defining privileges'''
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        '''Showing all privileges from user '''
        print("\nThis is your privileges:")
        for privilege in self.privileges:
            print(privilege)