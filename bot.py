import os
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if len(user_text) < 100:
        await update.message.reply_text(
        "📝 Отправьте текст подлиннее — минимум 100 символов."
        )
        return

    if len(user_text) > 4000:
        await update.message.reply_text(
        "📚 Текст слишком длинный — максимум 4000 символов."
        )
        return

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            instructions=(
                "Сократи текст пользователя. "
                "Сохрани основной смысл и всю важную информацию. "
                "Не добавляй факты, которых нет в исходном тексте. "
                "Верни только сокращённый текст."
            ),
            input=user_text
        )

        short_text = response.output_text
        await update.message.reply_text(short_text)

    except Exception as error:
        print("OpenAI error:", error)
        await update.message.reply_text(
            "⚠️ Не удалось обработать текст. Попробуйте ещё раз позже."
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я AI Text Shortener.\n\n"
        "Отправь мне большой текст, и я сокращу его, "
        "сохранив основной смысл и важную информацию."
    )

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot started...")
app.run_polling()