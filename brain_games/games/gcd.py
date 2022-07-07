"""Basic functions for GCD-game"""

import random
RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def get_question_answer():
    num1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    num2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)
