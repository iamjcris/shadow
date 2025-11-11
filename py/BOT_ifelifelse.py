while True: #to make the loop infinite
    user_input: str = input ('You: ')  # Example user input

    if user_input == 'hello':
        print('Bot: Hi there!')
    elif user_input == 'how are you?':
        print('Bot: I am fine, How about you?')
    elif user_input == 'bye': #you can have as many elif as you want
        print('Bot: Goodbye! Have a great day!')
    else:
        print('Bot: Sorry i dont understand that.')