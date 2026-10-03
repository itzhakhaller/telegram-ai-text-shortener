# AI Text Shortener Bot

A Telegram bot that shortens long texts using the OpenAI API while preserving the main meaning and important information.

## Features

- Accepts text through Telegram
- Summarizes long text using AI
- Preserves the original meaning
- Does not add information that is not present in the source text
- Checks minimum and maximum text length
- Handles OpenAI API errors
- Supports the `/start` command

## Technologies

- Python
- Telegram Bot API
- OpenAI API
- python-telegram-bot
- python-dotenv

## Installation

1. Install the required dependencies:

`pip install -r requirements.txt`

2. Create a `.env` file.

3. Add your API keys:

`TELEGRAM_TOKEN=your_telegram_token`

`OPENAI_API_KEY=your_openai_api_key`

4. Run the bot:

`python bot.py`

## Security

API keys are stored in the `.env` file and are excluded from GitHub using `.gitignore`.

## How it works

Telegram message → Python bot → OpenAI API → shortened text → Telegram response