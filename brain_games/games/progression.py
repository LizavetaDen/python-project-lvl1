"""Basic functions for Progression-game"""

import random
RULE_OF_GAME = 'What number is missing in the progression?'
MAX_NUMBER = 20
MIN_DIF = 1
MAX_DIF = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_progression(initial_term, common_difference, length):
    count = 1
    i = initial_term
    progression = [initial_term, ]
    while count <= length:
        i += common_difference
        progression.append(i)
        count += 1
    return progression


def get_question_gap(progression, missing_num):
    progression[missing_num] = '..'
    question = ' '.join(map(str, progression))
    return question


def get_question_answer():
    initial_term = random.randint(0, MAX_NUMBER)
    common_difference = random.randint(MIN_DIF, MAX_DIF)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(initial_term, common_difference, length)
    missing_num = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[missing_num])
    question = get_question_gap(progression, missing_num)
    return question, correct_answer
