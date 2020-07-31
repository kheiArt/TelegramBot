
from constants import *
from cv import cv_start, cv_name, cv_rating, cv_skip, cv_comment, cv_dontknow
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handlers import start_user, checking_number, send_rose_picture, user_coordinates, speaks_to_user, check_photo
import logging



logging.basicConfig(filename="bot.log", level=logging.INFO)


def main():
    mybot = Updater(KEY_BOTFATHER, use_context=True)

    dp = mybot.dispatcher

    CV = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(fill the questionnaire)$'), cv_start)
        ],
        states={
            "name": [MessageHandler(Filters.text, cv_name)],
            "rating": [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), cv_rating)],
            "comment": [
                CommandHandler('skip', cv_skip),
                MessageHandler(Filters.text, cv_comment)
        ]
        },
        fallbacks=[MessageHandler(Filters.text | Filters.video | Filters.photo | Filters.document | Filters.location, cv_dontknow)]
    )
    dp.add_handler(CV)
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("check", checking_number))
    dp.add_handler(CommandHandler("rose", send_rose_picture))
    dp.add_handler(MessageHandler(Filters.regex("^(Send a rose)$"), send_rose_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.photo, check_photo))
    dp.add_handler(MessageHandler(Filters.text, speaks_to_user))

    logging.info("The bot has started!")
    mybot.start_polling()
    mybot.idle()




if __name__ == "__main__":
    main()
