# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_openai
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

#load_dotenv()
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 3 sentences). No preamble, start your answer right away please.
            After the medical opinion, add the following labeled sections:
            Medicine: <short over-the-counter medicine suggestion>
            Workout: <short exercise or activity suggestion>
            Diet: <short diet or home tip suggestion>"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_openai(
        OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-1"
    )

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="gpt-4o"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")
    voice_filepath = text_to_speech_with_gtts(
        input_text=doctor_response, output_filepath="final.mp3"
    )

    return speech_to_text_output, doctor_response, voice_filepath


# Custom CSS to set background image
css = """
html, body, #root, .gradio-container, .gradio-app {
    height: 100%;
    background-image: url('a.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
"""


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath")  # <— use filepath instead of Temp.mp3
    ],
    title="AI Doctor with Vision and Voice",
    css=css
)

iface.launch(debug=True)

# http://127.0.0.1:7860
