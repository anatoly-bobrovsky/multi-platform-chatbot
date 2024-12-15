"""Redis Pub/Sub."""

import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Awaitable, Callable

import redis.asyncio as redis


class Channel(Enum):
    """Enumeration of available channels for Redis Pub/Sub."""

    TELEGRAM_BOT = "telegram_bot"
    CORE_BOT = "core_bot"
    WEBSOCKET_CHAT = "websocket_chat"


@dataclass
class Message:
    """Data class representing a message to be sent through Redis Pub/Sub.

    Attributes:
        text (str): The text content of the message.
        chat_id (str): The identifier for the chat.
        callback_channel (Channel): The channel to which the message should be sent.
    """

    text: str
    chat_id: str
    callback_channel: Channel

    def __str__(self) -> str:
        """Convert the message to a JSON string.

        Returns:
            str: JSON string representation of the message.
        """
        message_dict = asdict(self)
        message_dict["callback_channel"] = self.callback_channel.value
        return json.dumps(message_dict)


redis_client = redis.from_url("redis://redis:6379")


async def subscribe(channel: Channel, process_message: Callable[[Message], Awaitable[None]]) -> None:
    """Subscribe to a channel and process incoming messages.

    Args:
        channel (Channel): The channel to subscribe to.
        process_message (Callable[[Message], Awaitable[None]]): The function to process incoming messages.
    """
    async with redis_client.pubsub() as pubsub:
        await pubsub.subscribe(channel.value)

        while True:
            redis_message: dict = await pubsub.get_message(ignore_subscribe_messages=True)
            if redis_message is not None:
                message_dict = json.loads(redis_message["data"])
                message_dict["callback_channel"] = Channel(message_dict["callback_channel"])
                await process_message(Message(**message_dict))


async def publish(channel: Channel, message: Message) -> None:
    """Publish a message to a channel.

    Args:
        channel (Channel): The channel to publish the message to.
        message (Message): The message to be published.
    """
    await redis_client.publish(channel.value, str(message))
