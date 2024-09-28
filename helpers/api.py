import httpx
import logging
from typing import List, Dict, Any, Optional, TypedDict

logger = logging.getLogger(__name__)


class DefinitionInfo(TypedDict):
    definition: str
    example: Optional[str]  # Example can be None if not provided

class MeaningInfo(TypedDict):
    definitions: List[DefinitionInfo]

class WordDefinition(TypedDict):
    word: str
    pronunciation: Optional[str]  # Pronunciation can be None if not provided
    definitions: List[DefinitionInfo]

async def get_word_definition(word: str) -> WordDefinition | None:
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
                parsed_data:WordDefinition = {
                    "word": word_info.get("word"),
                    "pronunciation": word_info.get("phonetic"),
                    "definitions": [],
                }

                # Extract definitions
                for meaning in word_info.get("meanings", []):
                    for definition in meaning.get("definitions", []):
                        parsed_definition:DefinitionInfo = {
                            "definition": definition.get("definition"),
                            "example": definition.get(
                                "example", ""
                            ), 
                        }
                        parsed_data["definitions"].append(parsed_definition)

                return parsed_data  # Return structured data
            else:
                logger.warning(f"No data found for '{word}'.")
                return None
        else:
            logger.error(
                f"Failed to fetch definition for '{word}': {response.status_code}"
            )
            return None
