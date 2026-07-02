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
# -----------------------------
# SEND QUESTION
# -----------------------------

async def send_question(query, user_id):

    session = user_sessions[user_id]

    question = session["questions"][session["index"]]

    keyboard = [
        [
            InlineKeyboardButton(
                question["Option 1"],
                callback_data="1"
            )
        ],
        [
            InlineKeyboardButton(
                question["Option 2"],
                callback_data="2"
            )
        ],
        [
            InlineKeyboardButton(
                question["Option 3"],
                callback_data="3"
            )
        ],
        [
            InlineKeyboardButton(
                question["Option 4"],
                callback_data="4"
            )
        ]
    ]

    await query.message.reply_text(

        f"📖 Question {session['index']+1}/{TOTAL_QUESTIONS}\n\n"

        f"{question['Question']}",

        reply_markup=InlineKeyboardMarkup(keyboard)

    )


# -----------------------------
# START TEST
# -----------------------------

async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    current_day = 1

    questions = get_questions(current_day)

    if len(questions) == 0:

        await query.message.reply_text(

            "❌ Today's Test is not available."

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
