"""Basic functions for Calc-game"""

import random
RULE_OF_GAME = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 15


def get_question_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operators_list = ["+", "-", "*"]
    operation = random.choice(operators_list)
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    question = f'{num1} {operation} {num2}'
    return question, str(correct_answer)
