import aiohttp
import tracemalloc
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor


class OpenAIBot:
    def __init__(self, model, telegram_bot_token):
        self.model = model
        self.bot = Bot(token=telegram_bot_token)
        self.dp = Dispatcher(self.bot)

    async def handle_message(self, message: types.Message):
        message_text = message.text
        chat_id = message.chat.id
        print(message.text)
        await self.bot.send_chat_action(chat_id, types.ChatActions.TYPING)
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + 'Authorization_KEY',
                    },
                    json={
                        "model": self.model,
                        "messages": [{"role": "assistant", "content": f"{message_text}"}],
                        "temperature": 1,
                        "stop": None,
                    }
            ) as response:
                response_json = await response.json()
                print(response_json)
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
        model="gpt-3.5-turbo",
        telegram_bot_token="telegram_bot_token"
    )
    tracemalloc.start()
    bot.start()
