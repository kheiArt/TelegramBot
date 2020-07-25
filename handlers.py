
from glob import glob
from random import choice
from utils import get_emoji, get_random_number, main_keyboard



def start_user(update, context):
    print('/get started')
    context.user_data['emoji'] = get_emoji(context.user_data)
    update.message.reply_text(f"Hi user! {context.user_data['emoji']}", reply_markup=main_keyboard())


def speaks_to_user(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())


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
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_rose_picture(update, context):
    rose_photos_list = glob('rose/*.jpg')
    rose_pic_filename = choice(rose_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(rose_pic_filename, 'rb'), reply_markup=main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )



