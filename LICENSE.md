import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to open a web page
def open_webpage(url):
    webbrowser.open(url)

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function for listening and recognizing audio from microphone
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voices",voice[0].id)

rate=engine.getProperty('rate')   # getting details of current speaking rate
def Speak(text):
    engine.say(text)
    engine.runAndWait()

# Starting
current_time = datetime.datetime.now().time()
if current_time < datetime.time(12, 0):
    Speak("Hi sir, Good morning. What can I help You with?")
else:
    Speak("Hi sir, Good morning. What can I help You with?")

# Function to listen and process commands
def listen_and_execute():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)

            if "open Google" in command:
                open_webpage("https://www.google.com")
            elif "open YouTube" in command:
                open_webpage("https://www.youtube.com")
            elif "open Stack Overflow" in command:
                open_webpage("https://stackoverflow.com")
            elif "say something" in command:
                speak("Hello! I am your Python voice assistant.")
            else:
                speak("Command not recognized.")
        except sr.UnknownValueError:
            speak("Could you repeat. I couldnt understand you ")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")

# Continuously listen for commands
while True:
    listen_and_execute()
