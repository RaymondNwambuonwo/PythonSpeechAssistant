import speech_recognition as sr

# initialize recognizer class which is responsible for recognizing speech
r = sr.Recognizer()

# Using microphone as source of audio input
with sr.Microphone() as source:
    print("Say saomething")  # Prompt User
    audio = r.listen(source)  # Audio variable with source
    voice_data = r.recognize_google(audio)  # variable using recognize google
    print(voice_data)  # shows what user said
