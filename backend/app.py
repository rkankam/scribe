from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

# Charger le modèle Whisper local
model = pipeline("automatic-speech-recognition", model="openai/whisper-large-v2")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Save the file temporarily
        file_path = f'temp_{file.filename}'
        file.save(file_path)

        # Transcribe the audio using the local Whisper model
        transcript = model(file_path)

        # Remove the temporary file
        import os
        os.remove(file_path)

        return jsonify({'transcription': transcript['text']})

if __name__ == '__main__':
    app.run(debug=True)
