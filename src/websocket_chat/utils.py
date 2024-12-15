"""Utils."""

from fastapi import WebSocket

from pub_sub import Channel, Message, publish, subscribe


async def chat_ws_receiver(websocket: WebSocket, chat_id: str) -> None:
    """Receives messages from a WebSocket and publishes them to a specified channel.

    Args:
        websocket (WebSocket): The WebSocket connection to receive messages from.
        chat_id (str): The unique identifier for the chat session.
    """
    async for message in websocket.iter_text():
        await publish(channel=Channel.CORE_BOT, message=Message(text=message, chat_id=chat_id, callback_channel=Channel.WEBSOCKET_CHAT))


async def chat_ws_sender(websocket: WebSocket, chat_id: str) -> None:
    """Sends messages from a specified channel to a WebSocket.

    Args:
        websocket (WebSocket): The WebSocket connection to send messages to.
        chat_id (str): The unique identifier for the chat session.
    """
    async def process_message(message: Message) -> None:
        """Processes a message and sends it over the WebSocket if it matches the chat_id.

        Args:
            message (Message): The message to process.
        """
        if message.chat_id != chat_id:
            return

        await websocket.send_text(message.text)

    await subscribe(channel=Channel.WEBSOCKET_CHAT, process_message=process_message)
