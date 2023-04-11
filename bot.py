import aiohttp
import tracemalloc
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor


class OpenAIBot:
    def __init__(self, api_key, api_host, model, telegram_bot_token):
        self.api_key = api_key
        self.api_host = api_host
        self.model = model
        self.bot = Bot(token=telegram_bot_token)
        self.dp = Dispatcher(self.bot)

    async def handle_message(self, message: types.Message):
        message_text = message.text
        chat_id = message.chat.id
        await self.bot.send_chat_action(chat_id, types.ChatActions.TYPING)

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://openai80.p.rapidapi.com/chat/completions",
                    headers={
                        "content-type": "application/json",
                        "X-RapidAPI-Key": self.api_key,
                        "X-RapidAPI-Host": self.api_host
                    },
                    json={
                        "model": self.model,
                        "messages": [{
                            "role": "user",
                            "content": message_text
                        }]
                    }
            ) as response:
                response_json = await response.json()
                response_text = response_json["choices"][0]["message"]["content"]
                await self.bot.send_message(chat_id=chat_id, text=response_text, reply_to_message_id=message.message_id)

    def start(self):
        @self.dp.message_handler(Text(equals='/start'))
        async def start_handler(message: types.Message):
            await message.reply(
                "Hi! I am OpenAIBot Created API By https://t.me/AbdulrahmanTohamy How can I assist you?")

        self.dp.register_message_handler(self.handle_message, content_types=types.ContentTypes.TEXT)
        executor.start_polling(self.dp, skip_updates=True)


if __name__ == "__main__":
    bot = OpenAIBot(
        api_key="YOUR_RAPIDAPI_KEY_HERE",
        api_host="openai80.p.rapidapi.com",
        model="gpt-3.5-turbo",
        telegram_bot_token="YOUR_BOT_TOKEN_HERE"
    )
    tracemalloc.start()
    bot.start()

