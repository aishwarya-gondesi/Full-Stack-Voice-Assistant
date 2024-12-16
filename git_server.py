"""
This script serves as the backend server for the voice assistant application. 
It handles HTTP routes for:
1. Converting user speech to text.
2. Processing user text input through OpenAI GPT and returning responses.
3. Converting GPT responses to speech.

Run this file to start the Flask server.
"""

import base64
import json
from flask import Flask, render_template, request
from worker import speech_to_text, text_to_speech, openai_process_message
from flask_cors import CORS
import os

# Initialize Flask app and configure CORS to allow requests from any origin
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Route: Load the front-end interface
@app.route('/', methods=['GET'])
def index():
    """
    Render the main web interface for the voice assistant.
    """
    return render_template('index.html')

# Route: Convert user speech to text
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route(): 
    """
    Accept user speech (audio binary) and return transcribed text using Watson Speech-to-Text API.
    """
    print("Processing speech-to-text...")
    audio_binary = request.data  # Retrieve audio data from the request
    text = speech_to_text(audio_binary)  # Call speech_to_text function from worker.py
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print("Transcribed text:", text)
    return response

# Route: Process user message and return response in text and audio
@app.route('/process-message', methods=['POST'])
def process_prompt_route():
    """
    Process user input text through OpenAI GPT, return GPT's response in both text and audio formats.
    """
    user_message = request.json['userMessage']  # Extract user message
    print("User message:", user_message)
    voice = request.json['voice']  # Extract user's preferred voice
    print("Preferred voice:", voice)

    # Generate GPT response text
    openai_response_text = openai_process_message(user_message)
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])  # Clean empty lines

    # Convert GPT response to audio
    openai_response_speech = text_to_speech(openai_response_text, voice)
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')  # Encode to Base64

    # Return both text and audio response
    response = app.response_class(
        response=json.dumps({"openaiResponseText": openai_response_text, "openaiResponseSpeech": openai_response_speech}),
        status=200,
        mimetype='application/json'
    )
    print("GPT response (text and audio):", openai_response_text)
    return response

# Start the Flask server
if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')  # Accessible on localhost at port 8000
