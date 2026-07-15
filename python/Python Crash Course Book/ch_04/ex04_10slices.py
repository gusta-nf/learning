pizzas = ["Spicy sausage", "Portuguese-style", "Chicken w/ Brazilian cream cheese", "Chocolate"]
for pizza in pizzas:
    print("I like " + pizza + " pizza!")
    print("I really like pizza!")

# Modifications
print("The firsts three itens in list: " + str(pizzas[:3])) # For any value: the first three
print("The half of the list: " + str(pizzas[1:3])) # I had thought to use len // 2 to always the mid of the list, but the book don't introduce this
print("The last three itens in list: " + str(pizzas[-3:])) # For any value: the last three