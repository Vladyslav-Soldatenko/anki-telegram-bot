from telegram.ext import ApplicationBuilder, MessageHandler, filters
from helpers import handle_message, TELEGRAM_BOT_TOKEN,logger

def main() -> None:
    if TELEGRAM_BOT_TOKEN is None:
        logger.error("Bot token is missing. Make sure it's present in the .env file.")
        return

    # Create the Application (bot client)
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Add message handler to print received messages to the console
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
