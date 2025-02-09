from google.cloud import speech
from google.oauth2 import service_account
import io

# Function to transcribe audio to text using Google Speech API
def transcribe_audio(audio_file_path):
    # Set up credentials and client
    credentials = service_account.Credentials.from_service_account_file('../sorastts-b83f3a190855.json')
    client = speech.SpeechClient(credentials=credentials)

    # Read the audio file
    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    # Set up audio and config parameters for speech recognition
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # For WAV files
        sample_rate_hertz=24000,  # 24kHz
        language_code="en-US",
    )

    # Call the Google Speech-to-Text API
    response = client.recognize(config=config, audio=audio)

    # Process the response and return the transcribed text
    if response.results:
        return response.results[0].alternatives[0].transcript
    else:
        return "No speech detected"
