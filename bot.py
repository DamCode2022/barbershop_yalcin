from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot is online')

button_price = KeyboardButton('Услуги/Цены')
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb1.add(button_price)




@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer(text="Welcome to BarberBot from Yalcin!", reply_markup=kb1)
    await message.delete()

@dp.message_handler()
async def price(message: types.Message):
    if message.text == 'Услуги/Цены':
        await message.answer(text='price list')
        await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    pass



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
