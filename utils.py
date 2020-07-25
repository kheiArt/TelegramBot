from constants import USER_EMOJI
from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton



def get_emoji(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def get_random_number(user_number):
    random_number = randint(user_number - 10, user_number + 10)
    if user_number > random_number:
        message = f" Your number {user_number}, my number {random_number}, you won!"
    elif user_number == random_number:
        message = f" Your number {user_number}, my number {random_number}, draw!"
    else:
        message = f" Your number {user_number}, my number {random_number}, you lost!"
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['Send a rose', KeyboardButton('My coordinates', request_location=True)]])