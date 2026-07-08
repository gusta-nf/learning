# Parts of the text
dinner = ['Ada Lovelace', 'Alan Turing', 'George Boole']
greeting = "Hey, "
invitation = ", shall we get dinner, tonight?"
# Result
print(greeting + dinner[0] + invitation)
print(greeting + dinner[1] + invitation)
print(greeting + dinner[2] + invitation)
# Changing the list
print(dinner[1])
dinner.remove('Alan Turing')
dinner.insert(1, 'Richard Stallman')
print(greeting + dinner[0] + invitation)
print(greeting + dinner[1] + invitation)
print(greeting + dinner[2] + invitation)