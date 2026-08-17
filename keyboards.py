from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📋 Tasks", callback_data="tasks"),
            InlineKeyboardButton("💰 Wallet", callback_data="wallet")
        ],
        [
            InlineKeyboardButton("👥 My Referrals", callback_data="referrals"),
            InlineKeyboardButton("🛠️ Support", callback_data="support")
        ],
        [
            InlineKeyboardButton("🌐 Language", callback_data="language"),
            InlineKeyboardButton("🆕 Guide", callback_data="guide")
        ]
    ])


def wallet_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💵 Balance",
                callback_data="balance"
            )
        ],
        [
            InlineKeyboardButton(
                "➕ Deposit",
                callback_data="deposit"
            )
        ],
        [
            InlineKeyboardButton(
                "➖ Withdraw",
                callback_data="withdraw"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="home"
            )
        ]
    ])


def task_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📘 Facebook Task",
                callback_data="facebook"
            )
        ],
        [
            InlineKeyboardButton(
                "📸 Instagram Task",
                callback_data="instagram"
            )
        ],
        [
            InlineKeyboardButton(
                "📧 Gmail Task",
                callback_data="gmail"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="home"
            )
        ]
    ])
