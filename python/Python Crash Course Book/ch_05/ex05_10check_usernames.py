current_users = ['john', "Marie", 'SIR', 'gust' , 'man']
new_users = ['JOHN', 'marie', 'Joseph', 'chole', 'lady']
current_users_lower = [user.lower() for user in current_users] # I have to read again in the book List Comprehsion

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Username: ' +'"' + new_user.lower() + '"' + ' already exist! \tChoose another username.')
    else:
        print("Your username is avaible, " + new_user.lower() + "!")