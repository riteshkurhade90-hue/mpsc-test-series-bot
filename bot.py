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
from datetime import datetime
from config import TOTAL_QUESTIONS
from sheets import get_questions


async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    # Current Day (Temporary)
    current_day = 1

    questions = get_questions(current_day)

    if len(questions) == 0:
        await query.message.reply_text(
            "❌ Today's test is not available."
        )
        return

    user_sessions[user_id] = {
        "day": current_day,
        "questions": questions,
        "index": 0,
        "correct": 0,
        "wrong": 0,
        "start_time": datetime.now()
    }

    await send_question(query, user_id)
    await update.message.reply_text(
        "🎯 Welcome to MPSC Test Series\n\n"
        "Click the button below to start today's test.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
