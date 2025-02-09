import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # For handling CORS
from services.google_speech_to_text import transcribe_audio  # Your Google Speech-to-Text service
import logging

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow cross-origin requests from the frontend
CORS(app, origins=["http://localhost:3002"])  # Explicitly allow only your React frontend

# Set up logging for better error tracking
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return "Welcome to the Speech-to-Text API!"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Check if audio file is provided in the request
        if 'audio' not in request.files:
            logging.error('No audio file provided')
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        # Check if the file is an audio file (optional, can be skipped if not required)
        if not audio_file.filename.lower().endswith(('.wav', '.mp3', '.flac', '.m4a')):
            logging.error('Invalid file type')
            return jsonify({'error': 'Invalid audio file type'}), 400
        
        # Ensure 'temp' directory exists
        if not os.path.exists('temp'):
            os.makedirs('temp')

        # Save the audio file to a temporary location
        audio_file_path = os.path.join('temp', audio_file.filename)
        audio_file.save(audio_file_path)
        logging.info(f"Audio file saved to {audio_file_path}")

        # Call the Google Speech-to-Text service to transcribe the audio file
        transcription = transcribe_audio(audio_file_path)

        # Delete the temporary file after transcription
        os.remove(audio_file_path)
        logging.info(f"Temporary file {audio_file_path} removed")

        return jsonify({'transcription': transcription})

    except Exception as e:
        logging.error(f"Error during transcription: {str(e)}")
        return jsonify({'error': f"Error during transcription: {str(e)}"}), 500


if __name__ == '__main__':
    # Create 'temp' directory if it doesn't exist to save audio files
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Run the app on all available addresses (0.0.0.0) and port 5001
    app.run(debug=True, host='0.0.0.0', port=5001)
