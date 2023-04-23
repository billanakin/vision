import subprocess

def say(message, voice="default"):
    subprocess.run(["espeak", "-ven-us+f4", "-s150", message])
