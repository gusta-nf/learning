while True:
    age = input('\n\tCinema Ticket prices(0, Turn off)' + '\nHow old are you? ')
    age = int(age)
    if age == 0:
        print('Shutdown.')
        break
    elif age < 3:
        print('Ticket is free for you.')
    elif 3 <= age <= 12:
        print('Ticket is 10$ for you.')
    elif age > 12:
        print('Ticket is 15$ for you.')