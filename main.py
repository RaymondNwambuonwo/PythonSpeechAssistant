import speech_recognition as sr
import webbrowser
import time
from time import ctime

# initialize recognizer class which is responsible for recognizing speech
r = sr.Recognizer()

# Using microphone as source of audio input


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
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


def respond(voice_data):  # function for response from Claudia
    if 'what is your name' in voice_data:
        print('My name is Claudia')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What would you like to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('This is what I found regarding your search for ' + search)
    if 'get location' in voice_data:
        location = record_audio('What location would you like to find?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('This is the location of ' + location)


time.sleep(1)  # delays execution of funtion for given amount of time
print('Hey whats up, how can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
