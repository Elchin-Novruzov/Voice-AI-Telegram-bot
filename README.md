# Voice-AI-Telegram-bot

ChatGPT Telegram + ElevenLabs Voice Assistant
This project integrates OpenAI's ChatGPT API with Telegram and ElevenLabs voice synthesis to create an intelligent voice assistant. Users can interact with the assistant via Telegram, receiving text and voice responses powered by ChatGPT and ElevenLabs.
Features
- **Telegram Integration**: Chat with the assistant directly from Telegram.
- **Text-to-Speech**: Converts responses into realistic voice outputs using ElevenLabs.
- **Conversational AI**: Utilizes OpenAI's ChatGPT for natural and intelligent interactions.
- **Rich Media Support**: Handles text and voice seamlessly.
Prerequisites
- Python 3.9 or higher.
- A Telegram Bot API Token (create a bot via [BotFather](https://core.telegram.org/bots#botfather)).
- OpenAI API Key for ChatGPT.
- ElevenLabs API Key for text-to-speech synthesis.
Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatgpt-telegram-elevenlabs-voice-assistant.git
cd chatgpt-telegram-elevenlabs-voice-assistant
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Configure the environment variables:
Create a `.env` file in the project root and add:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```
Usage
1. Start the bot:
```bash
python main.py
```
2. Open Telegram and send messages to your bot. The bot will respond with text and, optionally, voice messages.
Project Structure
```
├── main.py                  # Main script to run the bot
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
├── .env                     # Environment variables (not included in the repo)
└── ...                      # Other files and scripts
```
Dependencies
- [gTTS](https://pypi.org/project/gTTS/) - Google Text-to-Speech
- [MoviePy](https://pypi.org/project/moviepy/) - Video editing library
- [Numpy](https://pypi.org/project/numpy/) - Scientific computing
- [OpenAI](https://pypi.org/project/openai/) - API client for OpenAI models
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/) - Telegram bot framework
- [ElevenLabsLib](https://pypi.org/project/elevenlabslib/) - ElevenLabs API wrapper
License
This project is licensed under the Our Licence.
Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.
Contact
For inquiries or support, reach out at [elchinnovruzovv@gmail.com](mailto:elchinnovruzovv@gmail.com).
