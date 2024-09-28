import logging
import os
from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging to help with debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from the .env file
TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")  

# Function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        user_message: str|None = update.message.text  # Type annotation for user_message
        print(f"Received message: {user_message}")  # Print the received message to the console
        await update.message.reply_text("Message received!")  # Reply to the user to acknowledge
    else:
        logger.warning("Received an update without a message.")

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
