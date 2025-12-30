import os
import requests
from datetime import datetime

from vega.commands import get_command

# ========= CONFIG =========
API_KEY = os.getenv("OPENAI_API_KEY")
USER_NAME = "Mr. Paul"

WAKE_MESSAGES = [
    "hey vega",
    "hey buddy",
    "are you there vega",
    "hi vega",
    "good morning vega",
    "good afternoon vega",
    "good evening vega"
]

# ========= CORE BRAIN =========
def think(prompt: str) -> str:
    prompt_lower = prompt.lower().strip()

    # --- Wake messages ---
    if prompt_lower in WAKE_MESSAGES:
        return f"Welcome back {USER_NAME}, what would you like to do today?"

    # --- Phase B: Command detection ---
    command = get_command(prompt_lower)
    if command:
        return (
            "I detected a system command.\n"
            f"I will run: {command}\n"
            "Please say YES to confirm."
        )

    # --- Safety check ---
    if not API_KEY:
        return "My API key is missing, Mr. Paul. Please configure it."

    # --- LLM request ---
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            f"You are VEGA, a personal AI assistant created by {USER_NAME}. "
                            f"Always address {USER_NAME} respectfully and directly."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
            },
            timeout=30,
        )

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"I encountered an error, {USER_NAME}: {str(e)}"
