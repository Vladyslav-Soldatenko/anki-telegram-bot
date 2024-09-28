# Anki Telegram Bot

A Telegram bot that fetches word definitions from an online dictionary API and stores them in a CSV file for use with Anki flashcards. You can import this CSV file to anki deck of your choice. It is also possible to extend this code and add support to AnkiConnect. This is personal project, so don't expect the best code or maintainability here. Main part was written with chatGPT since I'm not that proficient with Python. If you have suggestions - I'd be happy to collaborate

## Features

-   Fetches word definitions from the Free Dictionary API.
-   Supports fetching pronunciations and example sentences.
-   Appends fetched definitions to a CSV file for later use in Anki.
-   Easy integration with Telegram's messaging interface.

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [Configuration](#configuration)
-   [Contributing](#contributing)
-   [License](#license)
-   [Acknowledgements](#acknowledgements)

## Installation

Clone the repository:

git clone https://github.com/Vladyslav-Soldatenko/anki-telegram-bot.git
cd anki-telegram-bot

## Installation

Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`

### Install the required packages:

    pip install -r requirements.txt

### Create a .env file in the root directory to store your environment variables. Use the following format:

    TELEGRAM_BOT_TOKEN=your_bot_token_here
    CSV_PATH=/path/to/your/csv/folder

Run the bot:

    python ./main.py

In Telegram, find your bot by its username and start a conversation.

Send a word to the bot, and it will respond with the definition and save it to the specified CSV file.

## Configuration

    TELEGRAM_BOT_TOKEN: Your Telegram bot token obtained from BotFather.
    CSV_PATH: The directory path where the CSV file will be saved.

To run tests, use the following command:
pytest

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

## Acknowledgements

Free Dictionary API for providing the dictionary data.
