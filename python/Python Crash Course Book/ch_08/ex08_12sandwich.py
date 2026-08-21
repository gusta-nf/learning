def sandwich_itens(*items):
    print("This is items orders for your sandwich: ")
    for item in items:
        print("- " + item)

sandwich_itens('tomato', 'cheedar', 'bread', 'steak')
sandwich_itens('bread', 'steak')
sandwich_itens('bread')