import speech_recognition as sr
import openai
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import pyttsx3
# Set up OpenAI API key
openai.api_key = <>
# Function to recognize speech and convert it to text
def SpeechRecognizer():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as src:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(src)
        print("Listening...")
        audio = r.listen(src)
        print("Processing the audio...")
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return None
# Function to query OpenAI GPT with the given text
def ask_gpt(question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(command)
    engine.runAndWait()
# Main function
def main():
    print("Starting Speech Recognition...")
    question = SpeechRecognizer()
    if question:
        print(f"Querying GPT with the question: {question}")
        answer = ask_gpt(question)
        print(answer)
        SpeakText(answer)
if __name__ == "__main__":
    main()











