# def add(*numbers: float) -> float:
#     return sum(numbers)
#
# def mul(*numbers: float) -> float:
#     result = 1.0
#     for num in numbers:
#         result *= num
#     return result
#
# def sub(*numbers: float) -> float:
#     if not numbers:
#         return 0.0
#     result = numbers[0]
#     for num in numbers[1:]:
#         result -= num
#     return result

from functools import reduce
import operator

def add(*numbers: float) -> float:
    return sum(numbers) if numbers else 0.0


def mul(*numbers: float) -> float:
    return reduce(operator.mul, numbers) if numbers else 0.0

def sub(*numbers: float) -> float:
    return reduce(operator.sub, numbers) if numbers else 0.0

def div(*numbers: float) -> float:
    return reduce(operator.truediv, numbers) if numbers else 0.0

if __name__ == '__main__':
    print(add(40, 20, 100, 100))
    print(mul(20, 10))
    print(sub(500, 50, 30))
    print(div(150, 10))

# if __name__ == '__main__':
# bot_user = str ('ChatBot')
# print(f'\n{bot_user}: What can i do for you?')
#
# while True:
#     user_input: str = input(f'You: ').capitalize()
#     if user_input in ['Add', 'Addition', 'Can you add']:
#         print(f'{bot_user}: Sure! Please provide a two numbers to be added.')
#
#         try :
#             num1: float = float(input('First number: '))
#             num2: float = float(input('Second number: '))
#             print(f'{bot_user}: The sum of the number you input is {num1 + num2}')
#         except ValueError:
#             print(f'{bot_user}: Please enter a valid number input.')
#
#
#     elif user_input in ['Sub', 'Subtract', 'Can you sub']:
#         print(f'{bot_user}: Sure! Please provide a two numbers to be subtracted.')
#
#         try:
#             num1: float = float(input('First number: '))
#             num2: float = float(input('Second number: '))
#             print(f'{bot_user}: The sum of the number you input is {num1 - num2}')
#         except ValueError:
#             print(f'{bot_user}: Please enter a valid number input.')
#
#
#     elif user_input in ['Mul', 'Multiply', 'Can you mul']:
#         print(f'{bot_user}: Sure! Please provide a two numbers to be multiplied.')
#
#         try:
#             num1: float = float(input('First number: '))
#             num2: float = float(input('Second number: '))
#             print(f'{bot_user}: The sum of the number you input is {num1 * num2}')
#         except ValueError:
#             print(f'{bot_user}: Please enter a valid number input.')
#
#
#     elif user_input in ['Div', 'Divide', 'Can you div']:
#         print(f'{bot_user}: Sure! Please provide a two numbers to be divided.')
#
#         try:
#             num1: float = float(input('First number: '))
#             num2: float = float(input('Second number: '))
#             print(f'{bot_user}: The sum of the number you input is {num1 / num2}')
#         except ValueError:
#             print(f'{bot_user}: Please enter a valid number input.'1)
#
#     elif user_input in ['Thanks', 'Youre good','Galing ah']:
#         print(f'{bot_user}: Thank you for the compliment bro.')
#
#     else :
#         print(f'{bot_user}: Okay bye!')