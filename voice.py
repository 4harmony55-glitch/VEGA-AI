import speech_recognition as sr
from vega.brain import think
import pyttsx3

# Initialize TTS engine
tts = pyttsx3.init()

# Wake messages
wake_messages = [
    "hey vega",
    "hey buddy",
    "are you there, vega",
    "hi vega",
    "good morning vega",
    "good afternoon vega",
    "good evening vega"
]

def listen_and_respond():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    print("🎙️ VEGA listening... Say 'exit' to quit.")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)

            # Exit command
            if user_input.lower() == "exit":
                print("VEGA shutting down.")
                tts.say("Shutting down. Goodbye, Mr. Paul.")
                tts.runAndWait()
                break

            # Check for wake message
            if user_input.lower() in wake_messages:
                response = f"Welcome back Mr. Paul, what would you like to do today?"
            else:
                response = think(user_input)

            print("VEGA:", response)
            tts.say(response)
            tts.runAndWait()

        except sr.UnknownValueError:
            print("VEGA: Sorry, I did not understand that.")
            tts.say("Sorry, I did not understand that.")
            tts.runAndWait()
        except sr.RequestError as e:
            print(f"VEGA: Could not process audio; {e}")
            tts.say("I could not process your audio, Mr. Paul.")
            tts.runAndWait()


# Run VEGA automatically when executing this file
if __name__ == "__main__":
    listen_and_respond()
