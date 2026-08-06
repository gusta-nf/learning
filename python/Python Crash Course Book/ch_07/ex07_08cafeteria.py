sandwich_orders = ['Salad Sandwich', 'Double Sandwich', 'Chesse Sandwich']
finished_sandwiches = []
while sandwich_orders: #When sandwich_orders is empty, it's same of False
    current_sandwich = sandwich_orders.pop()
    print("I'm preparing your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print('\nThe following sandwiches have been finished:')
for sandwich in finished_sandwiches:
    print(sandwich.title())