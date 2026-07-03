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
# Just two guests now
apologize = "Sorry, you have to go, "
stay = ", you stay here for the dinner, ok?"
print("Unfortunely our table is smaller now")
print(apologize + dinner.pop())
print(apologize + dinner.pop())
print(apologize + dinner.pop())
print(apologize + dinner.pop())
print(dinner[0] + stay)
print(dinner[1] + stay)
# I recive a traceback before because I try del 0 and 1, but when I del 0, the 1 change to 0; However I fix this.
del dinner[1]
del dinner[0]
print(dinner)