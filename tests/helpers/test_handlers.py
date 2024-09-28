import os
import unittest
from unittest.mock import AsyncMock, patch, MagicMock
from telegram import Update
from telegram.ext import ContextTypes
from helpers import handle_message


class TestYourBotFunctionality(unittest.TestCase):
    @patch("helpers.get_word_definition", new_callable=AsyncMock)
    @patch("helpers.append_to_csv", new_callable=MagicMock)
    async def test_handle_message_success(
        self, mock_logger, mock_append_to_csv, mock_get_word_definition
    ):
        # Arrange
        mock_update = MagicMock(spec=Update)
        mock_update.message.text = "test"
        mock_get_word_definition.return_value = {
            "word": "test",
            "pronunciation": "tɛst",
            "definitions": [
                {
                    "definition": "A procedure intended to establish the quality, performance, or reliability of something."
                }
            ],
        }

        mock_context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

        # Act
        await handle_message(mock_update, mock_context)

        # Assert
        mock_logger.info.assert_called_with("Received message: test")
        mock_logger.info.assert_called_with(
            "Definition for 'test': {'word': 'test', 'pronunciation': 'tɛst', 'definitions': [{'definition': 'A procedure intended to establish the quality, performance, or reliability of something.'}]}"
        )
        mock_append_to_csv.assert_called_once()
        mock_update.message.reply_text.assert_called_with("Message received!")

    @patch("helpers.get_word_definition", new_callable=AsyncMock)
    async def test_handle_message_no_definition(
        self, mock_logger, mock_get_word_definition
    ):
        # Arrange
        mock_update = MagicMock(spec=Update)
        mock_update.message.text = "unknown_word"
        mock_get_word_definition.return_value = None
        mock_context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

        # Act
        await handle_message(mock_update, mock_context)

        # Assert
        mock_logger.warning.assert_called_with(
            "No definition found for 'unknown_word'."
        )
        mock_update.message.reply_text.assert_called_with("No definition found.")
