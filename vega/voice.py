import speech_recognition as sr
import subprocess

from vega.brain import think
from vega.commands import run_command

# ========= TTS (TERMUX NATIVE) =========
def speak(text: str):
    subprocess.run(["termux-tts-speak", text])

# ========= VOICE LOOP =========
def listen_and_respond():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ VEGA is online. Say something, Mr. Paul.")
    speak("VEGA is online, Mr. Paul.")

    # storage for pending command
    listen_and_respond.pending_command = None

    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            print("You:", text)

            # ---- Exit ----
            if text.lower() == "exit":
                speak("Goodbye Mr. Paul.")
                break

            # ---- Command confirmation ----
            if (
                text.lower() == "yes"
                and listen_and_respond.pending_command is not None
            ):
                output = run_command(listen_and_respond.pending_command)
                print(output)
                speak("Command executed.")
                listen_and_respond.pending_command = None
                continue

            # ---- Normal thinking ----
            reply = think(text)
            print("VEGA:", reply)
            speak(reply)

            # ---- Detect command proposal ----
            if "I will run:" in reply:
                listen_and_respond.pending_command = (
                    reply.split("I will run:")[1]
                    .split("\n")[0]
                    .strip()
                )

        except sr.UnknownValueError:
            print("VEGA: I didn’t catch that.")
            speak("I didn’t catch that, Mr. Paul.")

        except sr.RequestError:
            print("VEGA: Speech service unavailable.")
            speak("Speech service is unavailable, Mr. Paul.")

# ========= ENTRY POINT =========
if __name__ == "__main__":
    print("🔹 Phase A2 + B Voice Module Loaded")
    listen_and_respond()
