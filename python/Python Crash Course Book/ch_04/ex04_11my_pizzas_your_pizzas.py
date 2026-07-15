pizzas = ["Spicy sausage", "Portuguese-style", "Chicken w/ Brazilian cream cheese", "Chocolate"]

for pizza in pizzas:
    print("I like " + pizza + " pizza!")
    print("I really like pizza!")
    
# Modification
friend_pizzas = pizzas[:]
pizzas.append("Banana w/ Cinnamon")
friend_pizzas.append("Ice cream")

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nFavorite pizzas of my friend: ")
for pizza in friend_pizzas:
    print(pizza)