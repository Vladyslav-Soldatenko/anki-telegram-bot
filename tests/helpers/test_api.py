import unittest
from unittest.mock import AsyncMock, patch
from helpers import get_word_definition 
class TestGetWordDefinition(unittest.TestCase):

    @patch('httpx.AsyncClient.get', new_callable=AsyncMock)
    async def test_get_word_definition_success(self, mock_logger, mock_get):
        # Arrange
        word = "example"
        mock_response = {
            "word": "example",
            "phonetic": "/ɪɡˈzæmpəl/",
            "meanings": [
                {
                    "partOfSpeech": "noun",
                    "definitions": [
                        {
                            "definition": "A representative form or pattern.",
                            "example": "This is a good example of how to do it."
                        }
                    ]
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [mock_response]

        # Act
        result = await get_word_definition(word)

        # Assert
        self.assertEqual(result['word'], "example")
        self.assertEqual(result['pronunciation'], "/ɪɡˈzæmpəl/")
        self.assertEqual(len(result['definitions']), 1)
        self.assertEqual(result['definitions'][0]['definition'], "A representative form or pattern.")
        self.assertEqual(result['definitions'][0]['example'], "This is a good example of how to do it.")
        mock_logger.assert_not_called() 

    @patch('httpx.AsyncClient.get', new_callable=AsyncMock)
    async def test_get_word_definition_no_data(self, mock_logger, mock_get):
        # Arrange
        word = "unknownword"
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        # Act
        result = await get_word_definition(word)

        # Assert
        self.assertEqual(result, {})
        mock_logger.warning.assert_called_once_with("No data found for 'unknownword'.")

    @patch('httpx.AsyncClient.get', new_callable=AsyncMock)
    async def test_get_word_definition_api_failure(self, mock_logger, mock_get):
        # Arrange
        word = "failureword"
        mock_get.return_value.status_code = 404  # Simulate a 404 error

        # Act
        result = await get_word_definition(word)

        # Assert
        self.assertEqual(result, {})
        mock_logger.error.assert_called_once_with("Failed to fetch definition for 'failureword': 404")

if __name__ == '__main__':
    unittest.main()
