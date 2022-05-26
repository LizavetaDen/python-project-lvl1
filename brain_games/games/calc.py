"""Basic functions for Calc-game"""

import random


def introduction():
    return 'What is the result of the expression?'


def generate_request():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 5)
    sign = ["+", "-", "*"]
    operation = random.choice(sign)
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    request = f'{num1} {operation} {num2}'
    return (request, str(correct_answer))
