import subprocess

COMMAND_MAP = {
    "list my files": "ls",
    "show my files": "ls",
    "list files": "ls",
    "what files are here": "ls",
    "show directory": "ls",
    "current directory": "pwd",
    "where am i": "pwd",
}

def get_command(text: str):
    for phrase, command in COMMAND_MAP.items():
        if phrase in text:
            return command
    return None

def run_command(command: str):
    try:
        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result
    except Exception as e:
        return str(e)
