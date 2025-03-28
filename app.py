import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from transformers import pipeline
import speech_recognition as sr

app = Flask(__name__)

# ---------------------------
# AI Pipelines Initialization
# ---------------------------

# Pipeline for generating language exercises (using GPT-2 as an example)
exercise_generator = pipeline("text-generation", model="gpt2")

# Translation pipelines for selected languages.
# You can add more languages and corresponding pipelines as needed.
translation_pipelines = {
    "Spanish": pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es"),
    "French": pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr"),
    "German": pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
}

# ---------------------------
# Routes for the Application
# ---------------------------

@app.route('/')
def index():
    # Language selection page.
    languages = list(translation_pipelines.keys())
    return render_template('index.html', languages=languages)

@app.route('/select_language', methods=['POST'])
def select_language():
    language = request.form.get('language')
    # Redirect to dashboard with chosen language as a query parameter.
    return redirect(url_for('dashboard', language=language))

@app.route('/dashboard')
def dashboard():
    # Main dashboard where the user can generate exercises, translate phrases, and use speech recognition.
    language = request.args.get('language')
    return render_template('dashboard.html', language=language)

@app.route('/generate_exercise', methods=['POST'])
def generate_exercise():
    # Get user prompt from the form.
    prompt = request.form.get('prompt')
    # Generate an exercise (e.g., a conversation starter) using the text generation pipeline.
    result = exercise_generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    return jsonify({'exercise': result})

@app.route('/translate', methods=['POST'])
def translate():
    # Translate a given English text to the selected language.
    language = request.form.get('language')
    text_to_translate = request.form.get('text')
    if language in translation_pipelines:
        translation_pipeline = translation_pipelines[language]
        result = translation_pipeline(text_to_translate)[0]['translation_text']
    else:
        result = "Translation pipeline not available for this language."
    return jsonify({'translation': result})

@app.route('/speech_recognition', methods=['POST'])
def speech_recognition_endpoint():
    # Process uploaded audio file for speech recognition.
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided.'}), 400
    audio_file = request.files['audio_file']
    temp_filename = "temp_audio.wav"
    audio_file.save(temp_filename)
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_filename) as source:
        audio = recognizer.record(source)
    try:
        transcription = recognizer.recognize_google(audio)
    except Exception as e:
        transcription = f"Error: {e}"
    os.remove(temp_filename)
    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    # Run the app in debug mode (set debug=False for production).
    app.run(debug=True)
