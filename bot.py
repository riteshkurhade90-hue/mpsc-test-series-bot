import logging
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
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# -------------------------
# Runtime Memory
# -------------------------

user_sessions = {}

# -------------------------
# /start
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Start Today's Test",
                callback_data="start_test"
            )
        ]
    ]

    await update.message.reply_text(
        "🎯 Welcome to MPSC Test Series Bot\n\n"
        "📚 Daily 15 Questions\n"
        "⏳ Time Window : 2 Hours\n\n"
        "👇 Click below to start today's test.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
