"""Basic functions for GCD-game"""

import random
RULE_OF_GAME = 'Find the greatest common divisor of given numbers.'
LEFT_BORDER_NUMBER = 1
RIGHT_BORDER_NUMBER = 100


def gcd():
    while num2 != 0:
         num1, num2 = num2, num1 % num2
    return num1


def get_question_correctansw():
    num1 = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    num2 = random.randint(LEFT_BORDER_NUMBER, RIGHT_BORDER_NUMBER)
    question = (num1, num2)
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)
