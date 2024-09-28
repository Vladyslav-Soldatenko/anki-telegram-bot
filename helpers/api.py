# bot/api.py

import httpx
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

async def get_word_definition(word: str) -> Dict[str, Any]:
    """Fetch the definition of the given word from the Free Dictionary API and parse the response."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            
            # Extract relevant information
            if data:  # Ensure data is not empty
                word_info = data[0]  # Get the first entry
                parsed_data = {
                    "word": word_info.get("word"),
                    "pronunciation": word_info.get("phonetic"),
                    "definitions": []
                }

                # Extract definitions
                for meaning in word_info.get("meanings", []):
                    for definition in meaning.get("definitions", []):
                        parsed_definition = {
                            "definition": definition.get("definition"),
                            "example": definition.get("example", "")  # Use an empty string if example is not available
                        }
                        parsed_data["definitions"].append(parsed_definition)

                return parsed_data  # Return structured data
            else:
                logger.warning(f"No data found for '{word}'.")
                return {}
        else:
            logger.error(f"Failed to fetch definition for '{word}': {response.status_code}")
            return {}
