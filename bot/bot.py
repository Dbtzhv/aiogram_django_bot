from aiogram import Dispatcher, types, Bot, executor
from services import get_weather_data, create_telegram_message, get_top_headlines, get_commands_list
import asyncio



bot = Bot('')
dp = Dispatcher(bot)



@dp.message_handler()
async def cmd_start(message: types.Message):
    ans = await get_commands_list()

    if message.text.startswith(f"/{ans[0]['title']}"):
        await message.answer(ans[0]['text'])

    elif message.text.startswith(f"/{ans[1]['title']}"):
        await message.answer(ans[1]['text'])

    elif message.text.startswith(f"/{ans[2]['title']}"):
        words = message.text.split()

        if len(words) > 1:
            # Забираем последнее слово, которое будет представлять город
            city = words[-1]
            a = f'Погода в городе {city}: {get_weather_data(city)}'
            await message.answer(a)
            await create_telegram_message(message.message_id, message.from_user.id, message.chat.id, a)
        else:
            # Если город не указан, отправляем сообщение с инструкцией
            await message.answer('Пожалуйста, укажите город после команды /weather.')

    elif message.text.startswith(f"/{ans[3]['title']}"):
        a = get_top_headlines()
        await message.answer(a)
        await create_telegram_message(message.message_id, message.from_user.id, message.chat.id, a)
            


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)

    