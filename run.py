# -*- coding: utf-8 -*-
import os
import telebot

from util.log_helper import log
from dialog.engine import DialogEngine

dialog_engine = DialogEngine()

telegram_api_key = os.environ.get('TELEGRAM_TOKEN_PBOT')
bot = telebot.TeleBot(telegram_api_key)

@bot.message_handler(content_types=["text"])
def handleMessage(message):
    try:
        log('Handle message [chat_id=%d]: %s' % (message.chat.id, message.text))
        answer = dialog_engine.choose_answer(message)
        if answer:
            bot.send_message(message.chat.id, answer)

    except Exception as e:
        log('Error: ' + str(e))


if __name__ == '__main__':
    bot.polling(none_stop=True)
