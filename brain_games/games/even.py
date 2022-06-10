"""Basic functions for Even-game"""

import random
RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise "no".'
LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 1000


def is_even():
    return 'yes' if question % 2 == 0 else 'no'


def get_question_correctansw():
    question = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    correct_answer = is_even(question)
    return question, correct_answer
