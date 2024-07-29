# Jarvis Virtual Assistant

Jarvis is a Python-based virtual assistant designed to perform various tasks, similar to Alexa and Google Assistant. It can open web pages, play music, fetch news, and respond to user commands using OpenAI's GPT-3.5-turbo model.

## Features

- **Open Websites**: Command Jarvis to open Google, YouTube, Instagram, Facebook, or ChatGPT.
- **Play Music**: Ask Jarvis to play a song from a predefined music library.
- **Fetch News**: Get the latest tech news from TechCrunch.
- **AI Responses**: Jarvis can answer general queries using OpenAI's GPT-3.5-turbo model.
- **Voice Interaction**: Interact with Jarvis using voice commands.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `webbrowser` module (standard library)
- `openai` library
- `requests` library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install speechrecognition pyttsx3 openai requests
   ```

3. **Setup OpenAI API Key**:
   Replace `"sk-proj-v3VujGR8DyBDrvXIa0zGT3BlbkFJYpSZfv9EKQsR0jZuULx4"` with your OpenAI API key in `client.py` and `aiProcess` function in `main.py`.

4. **Setup News API Key**:
   Replace `"56c0ac03edcf4b4a978ec7d5e53bf810"` with your News API key in the `news` command section.

## Usage

1. **Run the Assistant**:
   ```bash
   python main.py
   ```

2. **Interact with Jarvis**:
   - Say "Jarvis" to wake up the assistant.
   - Give commands like "Open Google", "Play Skyfall", "What's the news?", etc.

## File Structure

- `main.py`: Main script to run the Jarvis assistant.
- `musicLibrary.py`: Contains a dictionary of songs and their YouTube links.
- `client.py`: Contains OpenAI client setup and a test completion.

## Example Commands

- **Open Websites**:
  - "Jarvis, open Google"
  - "Jarvis, open YouTube"

- **Play Music**:
  - "Jarvis, play Skyfall"

- **Fetch News**:
  - "Jarvis, what's the news?"

- **AI Responses**:
  - "Jarvis, what is coding?"

## Notes

- Ensure you have a working microphone and speakers for voice interaction.
- Customize the `musicLibrary.py` file to add more songs and their links.

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.


Enjoy using Jarvis! Your virtual assistant for daily tasks and more.
