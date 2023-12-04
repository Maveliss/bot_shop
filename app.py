from aiogram import types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from logging import basicConfig, INFO
from data.config import ADMINS
from loader import dp, bot, db
import handlers
from aiogram.types import Message

user_message = 'Пользователь'
admin_message = 'Админ'

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(user_message, admin_message)
    await message.answer('''Привет! 👋
    🤖 я бот Уолтер, я помогу тебе купить товары.
    🛍️ Чтобы перейти в каталог и выбрать необходимые товары, 
    для этого необходимо воспользоваться командой /menu.
    ❓ Возникли вопросы? Команда /help поможет связаться 
    с администратором, который поможет''', reply_markup=markup)

@dp.message_handler(commands='help')
async def cmd_help(message: Message):
    await message.answer('Этот функционал находится в стадии разработки')


@dp.message_handler(text = admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    if cid not in ADMINS:
        await message.answer('Вы не являетесь администратором', reply_markup=ReplyKeyboardRemove())
        # ADMINS.append(cid)
    else:
        await message.answer('Вы вошли в режим администратора', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text = user_message)
async  def user_mode(message: types.Message):
    cid = message.chat.id
    if cid in ADMINS:
        ADMINS.remove(cid)
    await message.answer('Вы вошли в режим пользователя', reply_markup=ReplyKeyboardRemove())




async def on_startup(dp):
    print('Бот запущен')
    basicConfig(level=INFO)
    db.create_tables()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)


