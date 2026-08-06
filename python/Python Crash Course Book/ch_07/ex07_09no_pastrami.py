sandwich_orders = [
    'Salad Sandwich', 'Pastrami Sandwich', 'Double Sandwich', 
    'Pastrami Sandwich', 'Chesse Sandwich', 'Pastrami Sandwich',
]
finished_sandwiches = []

print("Pastrami Sandwich is out," +
" we are canceled any Pastrami Sandwich orders.\n")

while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

while sandwich_orders: #When sandwich_orders is empty, it's same of False
    current_sandwich = sandwich_orders.pop()
    print("I'm preparing your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
    
print('\nThe following sandwiches have been finished:')
for sandwich in finished_sandwiches:
    print(sandwich.title()) 