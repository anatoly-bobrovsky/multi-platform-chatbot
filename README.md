# Multi-Platform Chatbot using Pub/Sub Pattern

## Introduction

This repository contains a multi-platform chatbot built using the Pub/Sub pattern. The chatbot is designed to be accessible across multiple communication channels, such as Telegram and WebSocket, making it easy to expand to other platforms in the future.

## Architecture

- **Core Bot**: Handles message processing logic, independent of any platform.
- **User Interaction Services**:
  - **Telegram Bot**: For communication via Telegram.
  - **WebSocket Chat**: For interaction via WebSocket.
- **Redis Pub/Sub**: Used for inter-service communication, ensuring independence, scalability, and simplicity in adding new platforms.

## Dependencies

- **Core Bot**:
  - `redis==5.2.1` for Pub/Sub communication.
- **Telegram Bot**:
  - `aiogram==3.15.0` for Telegram bot functionality.
  - `pydantic-settings==2.7.0` for environment management.
  - `redis==5.2.1` for Pub/Sub communication.
- **WebSocket Chat**:
  - `fastapi==0.115.6` for API development.
  - `redis==5.2.1` for Pub/Sub communication.
  - `uvicorn==0.33.0` for ASGI web server.
  - `websockets==14.1` for WebSocket connections.

## Deployment

- **Docker Compose**: Used to manage and run the services.
- **Services**:
  - `telegram_bot`: Handles Telegram interactions.
  - `websocket_chat`: Manages WebSocket connections.
  - `core_bot`: Processes messages and routes responses.
  - `redis`: Redis server for Pub/Sub communication.

## Usage

1. **Set up the environment**:
   - Create an external Redis volume: `docker volume create redis-data`.
   - Set the `TELEGRAM_BOT_TOKEN` in `docker-compose.yml` to your Telegram bot's token.

2. **Build and run the services**:
   - Execute `docker compose up -d --build` to start the services.

3. **Test the chatbot**:
   - Use a Telegram client to interact with the Telegram bot.
   - Use tools like Postman to test the WebSocket chat functionality.

