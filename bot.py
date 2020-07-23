
from emoji import emojize
from constants import *
from glob import glob
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging



logging.basicConfig(filename='bot.log', level=logging.INFO)

def start_user(update, context):
    print('/get started')
    update.message.reply_text('Hi user!')


def speaks_to_user(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def get_random_number(user_number):
    random_number = randint(user_number - 10, user_number + 10)
    if user_number > random_number:
        message = f" Your number {user_number}, my number {random_number}, you won!"
    elif user_number == random_number:
        message = f" Your number {user_number}, my number {random_number}, draw!"
    else:
        message = f" Your number {user_number}, my number {random_number}, you lost!"
    return message


def checking_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = get_random_number(user_number)
        except (TypeError, ValueError):
            message = "Please enter an integer."
    else:
        message = "Please enter a number."
    update.message.reply_text(message)


def send_rose_picture(update, context):
    rose_photos_list = glob('rose/*.jpg')
    rose_pic_filename = choice(rose_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(rose_pic_filename, 'rb'))



def main():
    mybot = Updater(KEY_BOTFATHER, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_user))
    dp.add_handler(CommandHandler("check", checking_number))
    dp.add_handler(CommandHandler("rose", send_rose_picture))
    dp.add_handler(MessageHandler(Filters.text, speaks_to_user))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
