class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:

        #initializers.attributes
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False #because ofc when buying a microwave it's initially turned off

#Method
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave: {self.brand} is already turned on. ')
        else:
            self.turned_on= True
            print(f'\nMicrowave: {self.brand} is now turned on. ')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave: {self.brand} is now turned off. ')
        else:
            self.turned_on = True
            print(f'Microwave: {self.brand} is already turned off. ')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds.')
        else:
            print(f'A Mystical force whispers: "Turn on you microwave first...".')

#Dunder Methods
    def __add__(self, other):
        return f'{self.brand} + {other.brand}'

    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'

    def __str__(self):
        return f'{self.brand} (Rating: {self.power_rating})'

    def __repr__(self):
        return f'Microwave: (Brand: {self.brand}, (Power rating: {self.power_rating})'


#the self in oop just refers to which ever instance we're currently using

smeg: Microwave = Microwave('Smeg', 'B')
# smeg.turn_on()
# smeg.turn_on()
# smeg.run(120)
# smeg.turn_off()
# smeg.run(30)

# print(f'\n{smeg}')
# print(smeg.brand)
# print(smeg.power_rating)
bosch: Microwave = Microwave('Bosch', 'C')
# bosch.turn_on()
# bosch.turn_on()

# print(f'\n{bosch}')
# print(bosch.brand)
# print(bosch.power_rating)

# print(smeg + bosch)
# print(smeg * bosch)

print(smeg)
print(bosch)

print(repr(smeg))
print(repr(bosch))