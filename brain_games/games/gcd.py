"""Basic functions for GCD-game"""

import random
RULE_OF_GAME = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def get_question_correctansw():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = (num1, num2)
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)
