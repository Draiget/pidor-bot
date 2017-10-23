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
        if type(message) == str:
            text = message
        elif type(message) == Message:
            text = message.text

        log('Answer message text: %s' % str(text))
        for question, answers in data.items():
            if re.match(question, text):
                return random.choice(answers)
        return None
