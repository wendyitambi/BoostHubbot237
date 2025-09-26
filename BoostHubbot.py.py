
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ==========================
# CONFIGURATION
# ==========================
BOT_TOKEN = "8418848148:AAGEif1eB8P7YIyg1fCsRd_6vkJHpPgDlI0"  # Replace with your BotFather token
ADMIN_ID = 7407668949  # Replace with your numeric Telegram ID

# ==========================
# COMMAND HANDLERS
# ==========================

# /start command
def start(update, context):
    update.message.reply_text(
        "👋 Welcome to BoostBot — your TikTok growth partner!\n\n"
        "Here you can boost your TikTok posts with real engagement.\n"
        "Use the menu below to get started 👇"
    )

# /services command
def services(update, context):
    update.message.reply_text(
        "🎵 TikTok Boosting Packages\n\n"
        "👥 Followers:\n"
        "- 1,500 followers = 5,000 XAF\n\n"
        "❤️ Likes:\n"
        "- 2,000 likes = 2,000 XAF (can be shared across posts)\n\n"
        "👀 Views:\n"
        "- 5,000 views = 2,500 XAF (can be shared across videos)\n\n"
        "💬 Custom Comments:\n"
        "- 10 comments = 2,000 XAF\n\n"
        "⚡ Delivery: Fast (within hours)\n"
        "💳 Payment: MTN MoMo / Orange Money (send screenshot after payment)"
    )

# /help command
def help_command(update, context):
    update.message.reply_text(
        "🆘 Help & FAQs\n\n"
        "1️⃣ Delivery: Usually within a few hours\n"
        "2️⃣ No password needed — just links\n"
        "3️⃣ Payment: MTN MoMo / Orange Money, upload proof\n"
        "4️⃣ Refunds: Only if we cannot deliver due to our error\n"
        "5️⃣ Splitting likes/views: You can split across posts/videos\n\n"
        "Need support? Use /contact"
    )

# /contact command
def contact(update, context):
    update.message.reply_text(
        "📬 Contact Support\n"
        "Reach us on Telegram: @YourUsername\n"
        "Or reply here with your issue and we will assist you."
    )

# /order command (starter)
def order(update, context):
    update.message.reply_text(
        "🛒 Let's place your order!\n\n"
        "Which service do you want?\n"
        "1️⃣ Followers\n"
        "2️⃣ Likes\n"
        "3️⃣ Views\n"
        "4️⃣ Custom Comments\n\n"
        "Please type your choice (e.g., 'Likes')."
    )

# Handle user messages (basic)
def handle_message(update, context):
    text = update.message.text.lower()
    chat_id = update.message.chat_id

    # Forward order details to admin automatically
    if text.startswith(("followers", "likes", "views", "comments")):
        order_message = f"🔔 New Order\n\nUser: @{update.message.from_user.username}\nService: {text}"
        context.bot.send_message(chat_id=ADMIN_ID, text=order_message)
        update.message.reply_text("✅ Your order has been received! Payment proof and links will be requested next.")
    else:
        update.message.reply_text("❌ Sorry, I didn't understand. Use /services or /order.")

# ==========================
# MAIN FUNCTION
# ==========================
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("services", services))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("order", order))

    # Message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
