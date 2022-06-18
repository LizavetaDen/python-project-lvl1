"""Basic functions for Even-game"""

import random
RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise "no".'
MIN_NUMBER = 1
MAX_NUMBER = 1000


def is_even(question):
    if question % 2 != 0:
        return False
    return True


def get_question_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
