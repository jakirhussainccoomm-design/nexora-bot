from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import init_db, create_user, get_balance
from keyboards import main_menu, wallet_menu, task_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    create_user(user.id)

    await update.message.reply_text(
        "🤖 **Welcome to Nexora!**\n\n"
        "👇 Choose an option:",
        reply_markup=main_menu()
    )


async def show_tasks(update, context):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "📋 **Which task would you like to do?**",
        reply_markup=task_menu()
    )


async def show_wallet(update, context):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "💰 **Wallet**\n\n"
        "Choose what you want 👇",
        reply_markup=wallet_menu()
    )


async def show_balance(update, context):
    query = update.callback_query
    await query.answer()

    data = get_balance(query.from_user.id)

    if not data:
        await query.edit_message_text(
            "❌ Balance information unavailable."
        )
        return

    (
        earn,
        deposit,
        pending,
        lifetime,
        referral,
        completed,
        review,
        rejected
    ) = data

    text = (
        "💵 **Your Balance**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🟢 **Earn Balance:** ৳{earn:.2f}\n"
        "    (Task income — withdrawable)\n\n"
        f"🔵 **Deposit Balance:** ৳{deposit:.2f}\n"
        "    (Deposited funds — for buying products)\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💸 **Pending Withdrawal:** ৳{pending:.2f}\n"
        f"💰 **Total Earned (Lifetime):** ৳{lifetime:.2f}\n"
        f"👥 **Referral Income:** ৳{referral:.2f}\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ **Completed Tasks:** {completed}\n"
        f"⏳ **In Review:** {review}\n"
        f"❌ **Rejected:** {rejected}"
    )

    await query.edit_message_text(text)


async def home(update, context):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🏠 **Main Menu**\n\n"
        "Choose an option 👇",
        reply_markup=main_menu()
    )


async def callback_router(update, context):
    query = update.callback_query

    routes = {
        "tasks": show_tasks,
        "wallet": show_wallet,
        "balance": show_balance,
        "home": home,
    }

    handler = routes.get(query.data)

    if handler:
        await handler(update, context)


def main():
    init_db()

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(callback_router)
    )

    print("🚀 Nexora Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
