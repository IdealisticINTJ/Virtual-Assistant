import speech_recognition as sr # Recognize speech
import playsound # To play an audio file
from gtts import gTTS # Google text-to-speech
import random
from time import ctime # To get time details
import webbrowser # To open browser
import ssl
import certifi
import time
import os # To remove created audio files
import pyttsx3
import bs4 as bs
import urllib.request
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

class assist:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # To initialize a recogniser
# Listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # Microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # To listen for the audio via source
        print("Done Listening.")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # To convert audio to text
        except sr.UnknownValueError: # Error: recognizer does not understand
            engine_speak('I did not get that. Could you try again?')
        except sr.RequestError:
            engine_speak('Sorry, Service down.') # Error: recognizer is not connected
        print(">>", voice_data.lower()) # Print what user said
        return voice_data.lower()

# To get string and make a audio file be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # Text to speech (voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # Save as mp3
    playsound.playsound(audio_file) # Play the audio file
    print(assist_obj.name + ":", audio_string) # Print what app said
    os.remove(audio_file) # Remove the audio file

def respond(voice_data):
    # 1: Greeting
    if there_exists(['Hey','Hi','Hello']):
        greetings = ["Hi. How can I help you?" + person_obj.name, "Hey, what's up?" + person_obj.name, "Go on. I'm listening." + person_obj.name, "I'm here to help!" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["What is your good name?","What's your name?","Tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {assist_obj.name}, {person_obj.name}") # Gets users name from voice input.
        else:
            engine_speak(f"My name is {assist_obj.name}. What's yours?") #Incase name hasn't been provided. 

    if there_exists(["My name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("Okay, I will remember that. " + person_name)
        person_obj.setName(person_name) # Remember the person name in person object.
    
    if there_exists(["What is my name?"]):
        engine_speak("Your name is " + person_obj.name +"That's what you told me anyway.")
    
    if there_exists(["your name should be"]):
        assist_name = voice_data.split("be")[-1].strip()
        engine_speak("Okay, I will remember that I've been named " + assist_name)
        assist_obj.setName(assist_name) # remember name in asis object

    # 3: Greeting
    if there_exists(["How are you?","How are you doing?"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name, "As happy as a clam! :)")

    # 4: Time
    if there_exists(["What's the time?","Tell me the time","What time is it?","What is the time?"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: Googling
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here's some information: " + search_term)
    
    if there_exists(["search"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on Google.")

    # 6: Searching YouTube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
    


    
     #7: Weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on Google:")
     

     
     #9 Calculations & Basic Arithmetic
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator. Try again.")
        
     
    
     #10 To search Wikipedia for definitions
    if there_exists(["definition of"]):
        definition=record_audio("What do you need the definition of?")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('I am sorry I could not find that definition. Please try a web search.')
            elif definitions[1]:
                engine_speak('Here is what I found: '+definitions[1])
            else:
                engine_speak ('Here is what I found: '+definitions[2])
        else:
                engine_speak("I am sorry I could not find the definition for "+definition)

    #11 Fetching user's current location 
    if there_exists(["What is my exact location?"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps.")    


    #12 To read some news
    if there_exists(['news']):
        
        url="https://www.ndtv.com"
        webbrowser.get().open(url)
        engine_speak('Here are some headlines from NDTV. Happy reading!')
        time.sleep(6)


    if there_exists(["Exit", "Quit", "Goodbye", "Bye", "Sayonara"]):
        engine_speak("bye")
        exit()

      

person_obj = person()
assist_obj = asis()
assist_obj.name = 'Ella'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # To get the voice input
    print("Done.")
    print("Q:", voice_data)
    respond(voice_data) # Respond

