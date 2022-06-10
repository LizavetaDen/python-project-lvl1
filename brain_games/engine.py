"""The overall logic of the game"""

import prompt
ROUNDS_COUNT = 3


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE_OF_GAME)
    i = 0
    while i <= ROUNDS_COUNT:
        question, correct_answer = game.get_question_correctansw()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        i += 1
        if i == ROUNDS_COUNT:
            print(f'Congratulations, {name}!')
            break
