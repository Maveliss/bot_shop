from aiogram.types import ReplyKeyboardMarkup

cancel_message = '🚫 Отменить'
back_message = '🔙 Назад'
all_right_message = '✅ Все верно'


def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)
    return markup


def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)
    return markup