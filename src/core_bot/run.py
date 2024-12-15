"""
Entrypoint for Core bot.
"""

import asyncio
from pub_sub import Channel, Message, subscribe, publish
from core_logic import get_echo_response


async def main() -> None:
    """
    Main function to run the Core bot.
    Subscribes to the CORE_BOT channel and processes incoming messages by sending back an echo response.
    """
    async def process_message(message: Message) -> None:
        """
        Process an incoming message by sending back an echo response.

        Args:
            message (Message): The incoming message to process.
        """
        await publish(channel=message.callback_channel, message=get_echo_response(message))

    await subscribe(channel=Channel.CORE_BOT, process_message=process_message)


if __name__ == "__main__":
    asyncio.run(main())
