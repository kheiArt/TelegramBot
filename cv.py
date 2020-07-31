from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard

def cv_start(update, context):
    update.message.reply_text(
        "What is your name? Write your first and last name ",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"

def cv_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Please write your first and last name")
        return "name"
    else:
        context.user_data["cv"] = {"name": user_name}
        reply_keyboard = [["1", "2", "3", "4", "5"]]
        update.message.reply_text(
            "Rate the bot on a scale of 1 to 5",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return "rating"

def cv_rating(update, context):
    context.user_data["cv"]["rating"] = int(update.message.text)

    update.message.reply_text(
        "Leave a comment in free form or skip this step enter /skip"
    )
    return "comment"

def cv_comment(update, context):
    context.user_data["cv"]["comment"] = update.message.text
    user_text = format_cv(context.user_data['cv'])

    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                              parse_mode=ParseMode.HTML)
    return ConversationHandler.END



def cv_skip(update, context):
    user_text = format_cv(context.user_data['cv'])

    update.message.reply_text(user_text, reply_markup=main_keyboard(),
                              parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def format_cv(cv):
    user_text = f"""<b>First Name Last Name:</b> {cv['name']}
    <b>Rating:</b> {cv['rating']}"""
    if cv.get('comment'):
        user_text += f"<b>Comment:</b> {cv['comment']}"

    return user_text

def cv_dontknow(update, context):
    update.message.reply_text("I do not understand")