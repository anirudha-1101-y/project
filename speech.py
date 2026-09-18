"""
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello i am ani..........")
engine.runAndWait()
"""
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)