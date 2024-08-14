import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import musiclibrary

recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open instagram and login to my page" in c.lower():
        speak("opening instagram and logging into nicobelix")
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "tell me a joke" in c.lower():
        speak(pyjokes.get_joke())
    elif "introduce yourself" in c.lower():
        speak("i am jarvis from jaaatt community , and there are only two types of people... , jaaatt and no jaaatt")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
if __name__ == "__main__":
    speak("initializing jarvis")
    while True:
        r=sr.Recognizer()
    
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listning...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes")
                with sr.Microphone() as source:
                    print("jarvis active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error ;{0}".format(e))

             
    
