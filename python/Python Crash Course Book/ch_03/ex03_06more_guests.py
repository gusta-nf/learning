# Parts of the text
dinner = ['Ada Lovelace', 'Alan Turing', 'George Boole']
greeting = "Hey, "
invitation = ", shall we get dinner, tonight?"
print(greeting + dinner[0] + invitation)
print(greeting + dinner[1] + invitation)
print(greeting + dinner[2] + invitation)
# A new table for dinner
print("\nOh, I find a bigger table for our dinner!\n")
# New guests
dinner.insert(0, 'Richard Stallman')
dinner.insert(2, 'Linus Torvalds')
dinner.append('Blaise Pascal')
print(greeting + dinner[0] + invitation)
print(greeting + dinner[1] + invitation)
print(greeting + dinner[2] + invitation)
print(greeting + dinner[3] + invitation)
print(greeting + dinner[4] + invitation)
print(greeting + dinner[5] + invitation)