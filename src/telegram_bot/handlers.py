"""Telegram Bot."""

from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message as TelegramMessage

from pub_sub import Channel, Message, publish

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: TelegramMessage) -> None:
    """
    Handles the /start command.

    Args:
        message (TelegramMessage): The message object containing the command.
    """
    await message.answer("Hello!")


@dp.message()
async def message_handler(message: TelegramMessage) -> None:
    """
    Handles all incoming messages and publishes them to the core bot channel.

    Args:
        message (TelegramMessage): The message object containing the text and chat information.
    """
    await publish(channel=Channel.CORE_BOT, message=Message(text=message.text, chat_id=str(message.chat.id), callback_channel=Channel.TELEGRAM_BOT))
