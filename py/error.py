a, b = 10, 'Fifteen'

try: #without this, the program will crash
    print(a + b)

# except Exception as e: #without this, the program will crash #bad practice to use Exception
#     print(f'\nSomething went wrong: {e}')
#     print(f'\nPlease enter a valid number input.')

#You can add multiple except blocks #not recomemended to use multiple except blocks, but it is not a bad thing to practice
except TypeError as e:
    print(f'Please enter a number in a form of a Integer or float!') #Do this practice instead of the one above

print('Continuing the program...')