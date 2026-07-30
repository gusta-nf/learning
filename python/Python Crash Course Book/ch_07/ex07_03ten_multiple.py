multi10 = input('Type a number to verify if its a 10 multiple or no: ')
multi10 = int(multi10)
if multi10 % 10: # multi10 % 10 == 0 for more readable, but this is my solution.
    print(str(multi10) + " isn't multiple of 10.") # !=0, so True
else:
    print(str(multi10) + " is multiple of 10.") # ==0, so False