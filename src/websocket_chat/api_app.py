"""API App entry point."""

import uvicorn
from fastapi import FastAPI, WebSocket
from starlette.concurrency import run_until_first_complete
from utils import chat_ws_receiver, chat_ws_sender

app = FastAPI(
    title="Chatbot",
    description="Pub/Sub Chatbot",
)


@app.websocket("/chatbot/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str) -> None:
    """
    WebSocket endpoint for chatbot communication.

    Args:
        websocket (WebSocket): The WebSocket connection object.
        chat_id (str): The unique identifier for the chat session.

    This function handles WebSocket connections for a chatbot. It accepts
    the WebSocket connection, then runs two asynchronous tasks concurrently:
    one for receiving messages from the client and another for sending
    messages to the client.
    """
    await websocket.accept()

    await run_until_first_complete(
        (chat_ws_receiver, {"websocket": websocket, "chat_id": chat_id}),
        (chat_ws_sender, {"websocket": websocket, "chat_id": chat_id}),
    )


if __name__ == "__main__":
    """
    Entry point for running the application.

    This script runs the FastAPI application using Uvicorn on all available network interfaces.
    """
    uvicorn.run(app, host="0.0.0.0")
