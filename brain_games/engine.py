"""The overall logic of the game"""

import prompt
COUNTS = 3


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.introduction())
    i = 0
    while i <= COUNTS:
        request, correct_answer = game.generate_request()
        print(f'Question: {request}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print('Correct!')   
    i += 1
    if i == COUNTS:
        print(f'Congratulations, {name}!')
        break
