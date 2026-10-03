# AI Text Shortener Bot

Telegram-бот, который сокращает длинные тексты с помощью OpenAI API, сохраняя основной смысл и важную информацию.

## Возможности

- Принимает текст через Telegram
- Сокращает текст с помощью AI
- Не добавляет информацию, которой нет в исходном тексте
- Проверяет минимальную и максимальную длину текста
- Обрабатывает ошибки OpenAI API
- Поддерживает команду /start

## Технологии

- Python
- Telegram Bot API
- OpenAI API
- python-telegram-bot
- python-dotenv

## Запуск

1. Установить зависимости:

pip install -r requirements.txt

2. Создать файл `.env`

3. Добавить:

TELEGRAM_TOKEN=your_telegram_token
OPENAI_API_KEY=your_openai_api_key

4. Запустить:

python bot.py

## Безопасность

API-ключи хранятся в `.env` и не загружаются в GitHub.