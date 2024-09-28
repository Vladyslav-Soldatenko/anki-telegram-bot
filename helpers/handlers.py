import os
import csv
from telegram import Update
from telegram.ext import ContextTypes
from .api import get_word_definition
from .config import CSV_PATH
from dotenv import load_dotenv
import logging

# Enable logging to help with debugging
logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming messages, fetches word definitions, and appends to CSV."""
    if update.message and update.message.text and CSV_PATH:
        user_message: str = update.message.text.strip()
        logger.info(f"Received message: {user_message}")
        definition = await get_word_definition(user_message)
        if definition:
            logger.info(f"Definition for '{user_message}': {definition}")
            front, back = prepare_csv_data(definition)
            append_to_csv(front, back)
            await update.message.reply_text("Message received!")  # Reply to the user
        else:
            logger.warning(f"No definition found for '{user_message}'.")
            await update.message.reply_text("No definition found.")  # Inform the user

def prepare_csv_data(definition: dict) -> tuple[str, str]:
    """Prepares the front and back content for the CSV from the word definition."""
    word = definition["word"]
    pronunciation = definition["pronunciation"]
    
    # Combine word and pronunciation for the front
    front = f"{word} ({pronunciation})"
    
    # Prepare back with definitions, checking for 'example' presence
    back = "\n".join(
        [
            f"{defn['definition']}" + (f"\nExample: {defn['example']}" if 'example' in defn and defn['example'] else "")
            for defn in definition["definitions"]
        ]
    )
    
    return front, back

def append_to_csv(front: str, back: str) -> None:
    """Appends the front and back data to the CSV file."""
    csv_file_path = os.path.join(CSV_PATH, "dictionary_definitions.csv") if CSV_PATH else ''
    file_exists = os.path.isfile(csv_file_path)

    try:
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            if not file_exists:
                # Write header if the file is new
                csv_writer.writerow(["Front", "Back"])
            csv_writer.writerow([front, back])  # Append the new row
        logger.info(f"Appended data for '{front.split(' ')[0]}' to CSV.")
    except Exception as e:
        logger.error(f"Failed to write to CSV: {e}")
