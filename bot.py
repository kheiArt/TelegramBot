
from constants import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start_user, checking_number, send_rose_picture, user_coordinates, speaks_to_user, check_photo
import logging



logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(KEY_BOTFATHER, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("check", checking_number))
    dp.add_handler(CommandHandler("rose", send_rose_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Send a rose)$'), send_rose_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.photo, check_photo))
    dp.add_handler(MessageHandler(Filters.text, speaks_to_user))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()




if __name__ == "__main__":
    main()
