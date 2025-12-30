import subprocess
import time
from .brain import think
from .speak import speak

WAKE_WORDS = [
    "vega",
    "hey vega",
    "are you there vega",
    "hey buddy"
]

def stop_mic():
    subprocess.run(
        ["pkill", "-f", "termux-microphone-record"],
        stderr=subprocess.DEVNULL
    )

def listen_loop():
    print("🟢 VEGA is active. Say a wake word or type 'exit'.")

    while True:
        stop_mic()

        subprocess.run([
            "termux-microphone-record",
            "-d", "4",
            "input.wav"
        ])

        # TEMP speech-to-text placeholder
        text = input("You (type speech for now): ").strip().lower()

        if text in ["exit", "quit", "shutdown"]:
            speak("Standing down, Mr. Paul.")
            break

        if any(wake in text for wake in WAKE_WORDS):
            response = think(text)
            print(f"\nVEGA: {response}\n")
            speak(response)

        time.sleep(0.5)

if __name__ == "__main__":
    listen_loop()
