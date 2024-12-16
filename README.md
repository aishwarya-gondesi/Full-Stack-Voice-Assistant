## Full-Stack-Voice-Assistant</br>
This project implements a full-stack voice assistant that integrates OpenAI GPT-3.5 for intelligent response generation and IBM Watson APIs for speech-to-text and text-to-speech functionalities. Users can interact with the assistant using voice input, receive intelligent responses, and hear the assistant's replies in natural speech.</br>

### Features </br>
Speech-to-Text Conversion: Uses IBM Watson Speech-to-Text API to transcribe user audio input into text.</br>
Intelligent Responses: Processes user input through OpenAI GPT-3.5 to generate contextual and meaningful responses.</br>
Text-to-Speech Conversion: Converts GPT-generated responses into speech using IBM Watson Text-to-Speech API.</br>
User-Friendly Web Interface: Accessible through a browser, enabling seamless interaction with the assistant.</br>

### Technologies Used </br>
Python: Backend programming language.</br>
Flask: Web framework for managing routes and backend logic.</br>
OpenAI GPT-3.5: For natural language processing and intelligent responses.</br>
IBM Watson Speech-to-Text API: For converting audio input to text.</br>
IBM Watson Text-to-Speech API: For converting text responses into audio.</br>
HTML/CSS/JavaScript: For building an interactive and responsive user interface.</br>

## Set Up Environment

### Install required dependencies:</br>
pip install -r requirements.txt

### Configure API Keys</br>
OpenAI API Key: Replace YOUR_OPENAI_API_KEY in worker.py with your OpenAI API key.</br>
IBM Watson APIs: Replace base_url placeholders in worker.py with your IBM Watson Speech-to-Text and Text-to-Speech API base URLs.</br>

## Running the Application </br>
Start the server with:</br>
python server.py</br>

Access the web interface by launching application.</br>
