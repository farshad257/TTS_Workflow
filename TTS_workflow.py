import os
import gradio as gr
from openai import OpenAI  # Make sure openai is installed: pip install -U openai
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client with AvalAI API
client = OpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key= os.getenv('AVAL_API_KEY')
)

# Function to generate speech and return audio file
def text_to_speech(text):
    speech_file_path = "./Generated_Media/Generated_files_gradio/generated_speech.mp3"  # Output file

    try:
        # Generate speech using AvalAI API
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )

        # Save the generated speech to a file
        # response.stream_to_file(speech_file_path)
        response.write_to_file(speech_file_path)

        return speech_file_path  # Returning the file path for playback & download

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=text_to_speech,
    inputs=gr.Textbox(label="Enter text..."),
    outputs=gr.Audio(label="Generated Voice:"),
    title="🗣️Generate voice based on entered text by AI (TTS)",
    description="You can generate voice of desired text by AI TTS model.",
)

# Launch the web app
iface.launch(share=True)
