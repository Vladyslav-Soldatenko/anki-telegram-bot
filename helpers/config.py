import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging to help with debugging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from the .env file
TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")
CSV_PATH: str | None = os.getenv("CSV_PATH")
