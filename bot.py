from datetime import datetime

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import (
    BOT_TOKEN,
    TOTAL_QUESTIONS,
)

from sheets import (
    get_questions,
    save_result,
    get_top3,
)

# -----------------------------
# USER SESSIONS
# -----------------------------

user_sessions = {}

# -----------------------------
# /START COMMAND
# -----------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Start Today's Test",
                callback_data="start_test"
            )
        ]
    ]

    text = (
        "🎯 *MPSC Test Series*\n\n"
        "✅ Total Questions : 15\n"
        "⏱ Time : 2 Hours\n"
        "📊 Result after submission\n\n"
        "👇 Click below to start today's test."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
