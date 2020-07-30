from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

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