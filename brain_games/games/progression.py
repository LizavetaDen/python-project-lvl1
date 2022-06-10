"""Basic functions for Progression-game"""

import random
RULE_OF_GAME = 'What number is missing in the progression?'
MAX_NUMBER = 20
MIN_DIF = 1
MAX_DIF = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression():
    initial_term = random.randint(0, MAX_NUMBER)
    common_difference = random.randint(MIN_DIF, MAX_DIF)
    lenght = random.randint(MIN_LENGTH, MAX_LENGTH)
    return [str(initial_term + common_difference * (i - 1))
            for i in range(lenght)]


def get_question_correctansw():
    progression = generate_progression()
    missing_num = random.randint(0, len(progression) - 1)
    correct_answer = progression[missing_num]
    progression[missing_num] = '..'
    question = ' '.join(progression)
    return question, correct_answer
