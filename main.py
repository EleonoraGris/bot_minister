from aiogram import *

bot = Bot(token='6198304169:AAGnqMO0-w1KDyIOWNnbPfmY1s_kAkMv4to')
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def hello(mes):
    await bot.send_message(mes.from_user.id, 'Привет! Я не министр, но передам ему все, что вы напишите.')
    await bot.send_message(mes.from_user.id, 'Вперед!')

@dp.message_handler()
async def hello(mes):
    await bot.send_message(-1002078246436, 'К вам новое обращение.')
    await bot.send_message(-1002078246436, mes.text)


if __name__ == '__main__':
    executor.start_polling(dp)
