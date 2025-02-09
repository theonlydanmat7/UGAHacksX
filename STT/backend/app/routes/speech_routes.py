from flask import Flask, request, jsonify
from backend.app.services.google_speech_to_text import transcribe_audio  # Import the function from google_speech_to_text

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Get the audio file from the request
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    
    # Save the audio file locally (you can adjust the file name here)
    file_path = 'temp_audio.wav'
    audio_file.save(file_path)

    # Call the transcribe_audio function
    try:
        transcription = transcribe_audio(file_path)
        return jsonify({"transcription": transcription})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
