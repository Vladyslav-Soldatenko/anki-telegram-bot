# bot/__init__.py

from .handlers import handle_message
from .api import get_word_definition
from .config import TELEGRAM_BOT_TOKEN, logger,CSV_PATH

__all__ = ['handle_message', 'get_word_definition', 'TELEGRAM_BOT_TOKEN', 'logger','CSV_PATH']
