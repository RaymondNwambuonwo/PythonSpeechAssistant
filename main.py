import speech_recognition as sr

# initialize recognizer class which is responsible for recognizing speech
r = sr.Recognizer()

# Using microphone as source of audio input


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)  # Audio variable with source
        voice_data = ''  # initialize voice data with empty string
        try:  # try block and this allows for unrecognizable speech and throws an error
            # variable using recognize google
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:  # this is if system does not understand what was said
            print("Sorry, I did not catch that")
        except sr.RequestError:
            print("My apologies, my speech is on the fritz")
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Claudia')


print("Hey whats up, how can I help you?")
voice_data = record_audio()
respond(voice_data)
