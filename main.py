import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


class person:
    name = ''

    def setName(self, name):
        self.name = name


def responsive(things):
    for thing in things:
        if thing in voice_data:
            return True


# initialize recognizer class which is responsible for recognizing speech
r = sr.Recognizer()

# Using microphone as source of audio input


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            claudia_speak(ask)
        audio = r.listen(source)  # Audio variable with source
        voice_data = ''  # initialize voice data with empty string
        try:  # try block and this allows for unrecognizable speech and throws an error
            # variable using recognize google
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:  # this is if system does not understand what was said
            claudia_speak("Sorry, I did not catch that")
        except sr.RequestError:
            claudia_speak("My apologies, my speech is on the fritz")
            print(f">> {voice_data.lower()}")  # print what user said
        return voice_data.lower()


def claudia_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # the text to speech(voice)
    r = random.randint(1, 30000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # saves file as mp3
    playsound.playsound(audio_file)  # plays the audio file
    print(audio_string)
    os.remove(audio_file)  # removes the audio file


def respond(voice_data):  # function for response from Claudia

    if responsive(['hey', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        claudia_speak(greet)

    if responsive(["what is your name", "what's your name", "tell me your name", "your name is"]):
        if person_obj.name:
            claudia_speak("my name is Claudia")
        else:
            claudia_speak("my name is Claudia. what's your name?")

    if responsive(["my name is", "I am", "I'm", "name's"]):
        person_name = voice_data.split("is")[-1].strip()
        claudia_speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)  # remember name in person object

    if responsive(["how are you", "how are you doing"]):
        claudia_speak(f"I'm very well, thanks for asking {person_obj.name}")

    if 'what time is it' in voice_data:
        claudia_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What would you like to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        claudia_speak(
            'This is what I found regarding your search for ' + search)

    if 'youtube' in voice_data:
        youtube = record_audio('What would you like to search on youtube?')
        url = 'https://www.youtube.com/results?search_query=' + youtube
        webbrowser.get().open(url)
        claudia_speak(
            'This is what I found regarding your search for ' + youtube)

    if 'get location' in voice_data:
        location = record_audio('What location would you like to find?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        claudia_speak('This is the location of ' + location)

    if 'exit' in voice_data:
        claudia_speak('goodbye')
        exit()


time.sleep(1)  # delays execution of funtion for given amount of time
claudia_speak('Hey whats up, how can I help you?')
person_obj = person()
while (1):
    voice_data = record_audio()
    respond(voice_data)
