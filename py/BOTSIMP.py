bot_name: str = 'Gray AI'
print(f'\nSup bro! I\'m {bot_name} How can i assist you today brother?')

while True: 
    user_input: str = input('You: ').capitalize()

    if user_input in ['Hi', 'Hello', 'Hey', 'Sup']:
        print(f'{bot_name}: Hi there! How can i help you?')

    elif user_input in ['How are you?', 'Hay', 'How are you']:
        print(f'{bot_name}: I am fine, How about you?')
    elif user_input in ['Im good', 'Good']:
        print(f'{bot_name}: That\'s great to hear! How can i assist you?')
    elif user_input in ['Bye', 'Goodbye', 'Nothing', 'Thanks']:
        print(f'{bot_name}: Okay Tangina mo kupal ka animal ka!, LAYAS!!!')
    elif user_input in ['Can you add?', 'Add', 'Addition', 'Can you add']:
        print(f'{bot_name}: Sure! Please provide a two numbers to be added.')

        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The sum of the number you input is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Please enter a valid number input.')
            
    elif user_input in ['Youre so good bro', 'Youre good','Galing ah']:
        print(f'{bot_name}: Thank you for the compliment bro.')

    else:
        print(f'{bot_name}: DI KA MAINTINDIHAN EH, AYUSIN MO.')
