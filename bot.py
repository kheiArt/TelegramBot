
from constants import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO)

def start_user(update, context):
    print('/get started')
    update.message.reply_text('Hi user!')



def main():
    mybot = Updater(KEY_BOTFATHER, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()







main()
