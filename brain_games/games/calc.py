"""Basic functions for Calc-game"""

import random
RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 15


def get_operator(num1, num2, operator):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    else:
        return str(num1 * num2)


def get_question_answer():
    num1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    num2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    operators = random.choice(['+', '-', '*'])
    question = f'{num1} {operators} {num2}'
    correct_answer = get_operator(num1, num2, operators)
    return question, correct_answer
