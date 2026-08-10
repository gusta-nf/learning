local = {}
while True:
    name = input("What's your name?\n")
    response = input(
    "If you could visit a place in the world, where would you go?\n"
    )
    
    local[name] = response
    repeat = input("Would other person like to answer?(yes/no)\n")
    if repeat == 'no':
        break

print("Resultados:")
for name, response in local.items():
    print(name + " would like to take a vacation in " + response + ".")