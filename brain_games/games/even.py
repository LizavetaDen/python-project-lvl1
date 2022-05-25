"""Basic functions for Even-game"""

import random


def introduction():
    return 'Answer "yes" if the number is even, otherwise "no".'


def generate_request():
    request = random.randint(1, 1000)
    correct_answer = 'yes' if request % 2 == 0 else 'no'
    return request, correct_answer
