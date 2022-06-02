"""Basic functions for Prime-game"""

import random


def introduction():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(request):
    if request < 1:
        return False
    for i in range(2, request):
        if request % i == 0:
            return False
    return True


def generate_request():
    request = random.randrange(1000)
    correct_answer = 'yes' if prime(request) else 'no'
    return request, correct_answer
