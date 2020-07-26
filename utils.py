from clarifai.rest import ClarifaiApp
from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton


from constants import *


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


def is_rose(file_name):
    app = ClarifaiApp(api_key=CLARIFAI_KEY)
    model = app.public_models.general_model
    response = model.predict_by_filename(file_name, max_concepts=5)
    if response['status']['code'] == 10000:
        for concept in response['outputs'][0]['data']['concepts']:
            if concept['name'] == 'rose':
                return True
    return False




if __name__ == "__main__":
    print(is_rose('rose/12240303_80d87f77a3_n.jpg'))
    print(is_rose('rose/5349860036_389d912fb7_n.jpg'))