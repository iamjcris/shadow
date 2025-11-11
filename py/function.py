def add (a: float, b: float) -> float: 
    print(f'\nadding {a} + {b}')
    return a + b

print(add(a=10 , b=15))
print(add(a=15 , b=30))

# print (add(10 , 15))
# print (add(15 , 30))


def greet(name: str ,  greeting: str = 'Hello') -> None:
    print(f'{name} , {greeting}')

greet(name= '\nAwra', greeting = 'Hi') #keyword arguments
greet(name= 'Koby') #default argument




