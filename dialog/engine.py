import random
import re

from telebot.types import Message
from dialog.answers import data
from util.log_helper import log


class DialogEngine(object):
    def __init__(self):
        log('Available answers data:')
        for question, answers in data.items():
            log(question + ' -> ' + str(answers))

    @staticmethod
    def choose_answer(message):
        text = None
        author = None
        senya_answers = ['sosi', 'zavali ebalo senya', 'zaebal', 'sosirui arsenii']
        if type(message) == str:
            text = message
        elif type(message) == Message:
            text = message.text
            author = message.from.username

        log('Answer message text: %s' % str(text))
        if author == '@Solidniy' or author == 'Solidniy':
            return random.choice(senya_answers)
        for question, answers in data.items():
            if re.match(question, text):
                return random.choice(answers)
        return None
