# AI-Based Language Learning Assistant

An interactive language learning platform that uses AI to provide personalized lessons, practice exercises, translation, and real-time pronunciation feedback. This project is inspired by popular language learning apps and leverages NLP, speech processing, and web technologies to deliver an engaging learning experience.

## Overview

The AI-Based Language Learning Assistant allows users to:
- **Select a target language:** Choose from a set of supported languages (e.g., Spanish, French, German).
- **Generate language exercises:** Use AI text generation to create practice exercises and conversation starters.
- **Translate phrases:** Convert English phrases into the selected target language using translation models.
- **Receive pronunciation feedback:** Upload audio samples to get transcription feedback and improve pronunciation.

This MVP (Minimum Viable Product) demonstrates core functionalities using Flask as the web framework, Hugging Face Transformers for language tasks, and the SpeechRecognition library for audio processing.

## Features

- **Language Selection:** Choose your desired language to learn.
- **Exercise Generation:** Generate practice exercises using AI-driven text generation (GPT-2).
- **Translation:** Translate English text to the target language using pre-trained translation pipelines.
- **Speech Recognition:** Upload a WAV audio file to receive transcription feedback, assisting with pronunciation.
- **Responsive Dashboard:** A web interface built with HTML, CSS, and JavaScript for an interactive user experience.

## Technologies Used

- **Backend:** Python, Flask
- **AI/NLP:** Hugging Face Transformers (GPT-2, Helsinki-NLP translation models)
- **Speech Processing:** SpeechRecognition library (Google Speech API)
- **Frontend:** HTML, CSS, JavaScript (jQuery)
- **Deployment:** Can be deployed on cloud platforms (Heroku, AWS, etc.)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/ai-language-learning-assistant.git
   cd ai-language-learning-assistant
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**

   ```bash
   pip install requirements.txt
   ```

## Usage

1. **Run the Application:**

   ```bash
   python app.py
   ```

2. **Open Your Browser:**

   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using the Language Learning Assistant.

3. **Workflow:**
   - **Select Language:** Choose the language you want to learn on the homepage.
   - **Dashboard:** On the dashboard, generate exercises by entering a prompt, translate text, or upload an audio file to test pronunciation.
   - **Receive Feedback:** View AI-generated exercises, translation results, and transcription of your speech on the dashboard.
