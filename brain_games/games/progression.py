"""Basic functions for Progression-game"""

import random


def introduction():
    return 'What number is missing in the progression?'


def generate_request():
    starting_number = random.randrange(20)
    difference = random.randint(1, 10)
    length = random.randint(5, 10)
    missing_number = random.randint(0, length - 1)
    progression = [
        str(starting_number + difference * (i - 1))
        for i in range(length)]
    correct_answer = progression[missing_number]
    progression[missing_number] = '..'
    request = ' '.join(progression)
    return request, str(correct_answer)
