import speech_recognition as sr
import pywhatkit

def command():
    print("Loading Health GPT")
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, say something...")
        try:
            audio = recorder.listen(source, timeout=5)
            text = recorder.recognize_google(audio)
            print(f"You said: {text}\n")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
            return ""
        except sr.RequestError as e:
            print(f"Error accessing Google Speech Recognition service: {e}")
            return ""



if __name__== '__main__':
    while True:
        text = command()
        if "goodbye" in text or "okay bye" in text or "turn off" in text:
            print('See you later!')
            break
        elif any(keyword in text for keyword in ["health", "rash", "medicine", "pain", "sick", "feeling", "aches", "itch", "std"]):
            pywhatkit.search(text)
        else:
            print("Keyword not recognized. Please try again.")
