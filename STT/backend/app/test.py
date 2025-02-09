import os
from services.google_speech_to_text import transcribe_audio

def test_transcription(audio_file_path):
    try:
        print(f"Testing transcription for file: {audio_file_path}")
        transcription = transcribe_audio(audio_file_path)
        print("Transcription successful:")
        print(transcription)
    except Exception as e:
        print(f"Error during transcription: {e}")

if __name__ == "__main__":
    # Replace this with the actual path to the audio file you want to test
    audio_file_path = 'test_audio.wav'  # Update this path to a real audio file
    test_transcription(audio_file_path)
