"""Basic functions for Even-game"""

import random
RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise "no".'
MIN_NUMBER = 1
MAX_NUMBER = 1000


def is_even(question):
    return 'yes' if question % 2 == 0 else 'no'


def get_question_correctansw():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(question)
    return question, correct_answer
