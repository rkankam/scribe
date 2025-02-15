# Voice Recognition App

This repository contains the code for a voice recognition app built with Flask (backend) and HTML/CSS/JavaScript (frontend). The app uses the Whisper model from Hugging Face for transcribing audio recordings.

## Features

- Record audio from the microphone.
- Send the audio recording to the backend for transcription using Whisper.
- Display the transcription in a text area.
- Copy the transcription to the clipboard.

## Prerequisites

- Python 3.8 or later
- Node.js and npm (for frontend development)

## Setup

### Backend

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/voice_recognition_app.git
   cd voice_recognition_app/backend
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the Flask server:**
   ```sh
   python app.py
   ```

### Frontend

1. **Open the frontend files in your browser:**
   ```sh
   start chrome frontend/index.html
   ```

## Usage

1. **Start Recording:** Click the "Start Recording" button to begin recording audio from the microphone.
2. **Stop Recording:** Click the "Stop Recording" button to end the recording.
3. **View Transcription:** The transcription will appear in the text area once the processing is complete.
4. **Copy Transcription:** Click the "Copy" button to copy the transcription to the clipboard.

## Contributing

Feel free to open issues and pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
