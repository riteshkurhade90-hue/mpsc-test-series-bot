from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from config import BOT_TOKEN
from sheets import get_questions

# User Session
user_sessions = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📝 Start Today's Test",
                callback_data="start_test"
            )
        ]
    ]

    await update.message.reply_text(
        "🎯 Welcome to MPSC Test Series\n\n"
        "Click the button below to start today's test.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
