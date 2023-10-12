import speech_recognition as sr
import webbrowser
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_it',
                                               client_secret='your_client_secret',
                                               redirect_uri='your_redirect_url',
                                               scope='user-library-read user-modify-playback-state'))

# Initialize pyttsx3 and customize the voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Function to open a web page
def open_webpage(url):
    webbrowser.open(url)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to play a song from Spotify
def play_spotify_song(song_name):
    results = sp.search(q=song_name, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
    else:
        speak(f"Sorry, I couldn't find the song '{song_name}' on Spotify.")

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
                speak("Hello! I am Jarvis")
            elif "play song on Spotify" in command:
                speak("Sure, what's the name of the song you'd like to play?")
                with sr.Microphone() as song_source:
                    audio = recognizer.listen(song_source)
                    song_name = recognizer.recognize_google(audio).lower()
                play_spotify_song(song_name)
            else:
                speak("Command not recognized.")
        except sr.UnknownValueError:
            speak("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")

# Get the current time
current_time = datetime.datetime.now().time()

# Greet the user based on the time
if current_time < datetime.time(12, 0):
    speak("Hi sir, Good morning. What can I help you with?")
else:
    speak("Hi sir, Good afternoon. What can I help you with?")

# Continuously listen for commands
while True:
    listen_and_execute()
