import speech_recognition as sr

# initialize recognizer class which is responsible for recognizing speech
r = sr.Recognizer()

# Using microphone as source of audio input
with sr.Microphone() as source:
    print("Say saomething")  # Prompt User
    audio = r.listen(source)  # Audio variable with source
   # try block and this allows for unrecognizable speech and throws an error
    try:
        # variable using recognize google
        voice_data = r.recognize_google(audio)
        print(voice_data)  # shows what user said
    except sr.UnknownValueError:
        print("Sorry, I did not catch that")
    except sr.RequestError:
        print("My apologies, my speech is on the fritz")
