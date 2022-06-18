"""Basic functions for Prime-game"""

import random
RULE_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question < 1:
        return False
    for i in range(2, question):
        if question % i == 0:
            return False
    return True


def get_question_answer():
    question = random.randrange(1000)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
