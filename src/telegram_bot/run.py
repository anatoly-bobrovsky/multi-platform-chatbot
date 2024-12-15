"""Entrypoint for Telegram bot."""

import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from env_settings import env
from handlers import dp

from pub_sub import Channel, Message, subscribe


async def main() -> None:
    """
    Main function to initialize and run the Telegram bot.

    This function sets up the bot with the token and default properties,
    defines a message processing function, and starts both the message
    subscription and the polling for updates.
    """
    bot = Bot(token=env.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    async def process_message(message: Message) -> None:
        """
        Process a message by sending it to the appropriate chat.

        Args:
            message (Message): The message object containing chat_id and text.
        """
        await bot.send_message(chat_id=int(message.chat_id), text=message.text)

    await asyncio.gather(
        subscribe(channel=Channel.TELEGRAM_BOT, process_message=process_message), dp.start_polling(bot)
    )


if __name__ == "__main__":
    asyncio.run(main())
