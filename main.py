import pygame
import speech_recognition as sr
import pywhatkit

def draw_text(screen, font, text):
    screen.fill((255, 255, 255))  # Fill the screen with white color
    text_surface = font.render(text, True, (0, 0, 0))  # Render the text with black color
    screen.blit(text_surface, (100, 200))  # Position the text on the screen

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

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Health GPT Window")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text = command()
        if "goodbye" in text or "okay bye" in text or "turn off" in text:
            print('See you later!')
            break
        elif any(keyword in text for keyword in ["health", "rash", "medicine", "pain", "sick", "feeling", "aches", "itch", "std"]):
            pywhatkit.search(text)
        else:
            print("Keyword not recognized. Please try again.")

        draw_text(screen, font, "Say something related to health....")
        pygame.display.flip()
        clock.tick(30)
