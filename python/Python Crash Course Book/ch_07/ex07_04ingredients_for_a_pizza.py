active = True
while active:
    ingredient = input("What ingredient do you add in your pizza?\n (Type 'quit' to exit the program)\n")
    if ingredient != 'quit':
        print("I'm going to add " + ingredient + " to your pizza.")
    else:
        active = False