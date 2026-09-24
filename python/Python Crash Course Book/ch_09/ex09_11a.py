''' Importing a Class with a Class in your attribute'''
import users

master = users.Admin("Gustavo", "Fernandez", "Owner", "77", 22)

master.privileges.show_privileges()