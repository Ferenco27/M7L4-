import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 5
sample_rate = 44100
print("🎙️ Please Talk...")
recording = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype="int16")

sd.wait()
wav.write("audio.wav", sample_rate, recording)
print("⏳ Processing audio...")
recognizer = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio, language="en-GB")
    print("You said:", text)
    translator = Translator()

    print("\nAvailable examples:")
    print("es = Español")
    print("en = English")
    print("fr = Frances")
    print("de = Deutsch")
    print("it = Italiano")
    print("pt = Portugues")

    target_lang = input("\nEnter target language code: ")

    translated = translator.translate(text, dest=target_lang)

    print("\n🔁 Translated text:")
    print(translated.text)

except Exception as e:
    print("Unrecognizable audio or connection error.")
    print("Details:", e)
