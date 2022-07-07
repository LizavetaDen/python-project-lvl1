"""Basic functions for Even-game"""

import random
RULES = 'Answer "yes" if the number is even, otherwise "no".'
MIN_NUMBER = 1
MAX_NUMBER = 1000


def is_even(question):
    return question % 2 == 0


def get_question_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
