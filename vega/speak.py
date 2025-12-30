import subprocess

def speak(text):
    subprocess.run([
        "termux-tts-speak",
        text
    ])
