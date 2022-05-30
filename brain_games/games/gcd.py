"""Basic functions for GCD-game"""

import random


def introduction():
    return 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1


def generate_request():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    request = (num1, num2)
    correct_answer = gcd(num1, num2)
    return (request, str(correct_answer))
