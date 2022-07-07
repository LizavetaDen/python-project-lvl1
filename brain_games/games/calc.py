"""Basic functions for Calc-game"""

import operator
import random
from random import choice
RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 15


def get_question_answer():
    num1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    num2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    operators_list = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    operation = choice(list(operators_list.keys()))
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    question = f'{num1} {operation} {num2}'
    return question, str(correct_answer)
