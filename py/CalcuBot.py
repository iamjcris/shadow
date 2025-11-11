
bot_user = str ('CalcupalBot')
print(f'\n{bot_user}: Hi kupal, What do you want? [Addition? Subtraction? Multiplication? Division?]')

while True:
    user_input: str = input(f'You: ').capitalize()
    if user_input in ['Add', 'Addition', 'Can you add']:
        print(f'{bot_user}: Sure! Please provide a two numbers to be added.')

        try :
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_user}: The sum of the number you input is {num1 + num2}')
        except ValueError:
            print(f'{bot_user}: Please enter a valid number input.')


    elif user_input in ['Sub', 'Subtract', 'Can you sub']:
        print(f'{bot_user}: Sure! Please provide a two numbers to be subtracted.')

        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_user}: The sum of the number you input is {num1 - num2}')
        except ValueError:
            print(f'{bot_user}: Please enter a valid number input.')


    elif user_input in ['Mul', 'Multiply', 'Can you mul']:
        print(f'{bot_user}: Sure! Please provide a two numbers to be multiplied.')

        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_user}: The sum of the number you input is {num1 * num2}')
        except ValueError:
            print(f'{bot_user}: Please enter a valid number input.')


    elif user_input in ['Div', 'Divide', 'Can you div']:
        print(f'{bot_user}: Sure! Please provide a two numbers to be divided.')

        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_user}: The sum of the number you input is {num1 / num2}')
        except ValueError:
            print(f'{bot_user}: Please enter a valid number input.')

    elif user_input in ['Thanks','You\'re good','Galing ah']:
        print(f'{bot_user}: Thank you for the compliment bro.')

    elif user_input in ['Masarap ba ako?', 'Masarap ba si jm']:
        print(f'{bot_user}: Oo naman potaena, yummy yan si boss')

    elif user_input in ['Weh', 'Sus', 'Buladas']:
        print(f'{bot_user}: Oo nga tnginamo kakulit mo, wag mo akong ginaganyan ganyan!')

    else :
        print(f'{bot_user}: Oh ulul, wala sa pagpipilian yan!')