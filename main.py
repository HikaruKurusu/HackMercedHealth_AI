import speech_recognition as sr
import pyaudio
import pywhatkit
import wikipedia
import webbrowser

def command():
    print("Loading Health GPT")
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, say something...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print("")
    print(f"You said: {text}")
    print("")
    return text



if __name__== '__main__':

    while True:
        text = command()
        if "goodbye" in text or "okay bye" in text or "turn off" in text:
            print ('see you later!')
            break
        if "youtube" in text.lower():
            # pywhatkit.playonyt("youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
        elif "google" in text.lower():
            pywhatkit.search(text)
        elif "youtube for" in text.lower():
            pywhatkit.search(text)
        # text = ""
        # elif "search" in text.lower():
        #     result = wikipedia.summary(text, sentences=2)
        #     print(result)
        # elif "health" in text.lower():
        #     result = wikipedia.summary(text, sentences=2)
        #     print(result)
        # elif "what does" in text.lower():
        #     result = wikipedia.summary(text, sentences=2)
        #     print(result)
        # elif "how do i know" in text.lower():
        #     result = wikipedia.summary(text, sentences=2)
        #     print(result)
        # else:
        #     print("sorry i didnt get that say that again")
