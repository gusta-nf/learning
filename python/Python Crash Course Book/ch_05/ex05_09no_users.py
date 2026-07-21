users = []
if users: #Modification
    for user in users:
        if user == 'admin':
            print('Hello admin, do you want to see the reports?')
        else:
            print('Hello ' + user + ', thank you for logon again.')
else: #Modification
    print('We need to find new users.')
#Old code
users = ['admin', 'Gustavo', 'Rodolfo', 'Felipe', 'Joao']
for user in users:
    if user == 'admin':
        print('Hello admin, do you want to see the reports?')
    else:
        print('Hello ' + user + ', thank you for logon again.')