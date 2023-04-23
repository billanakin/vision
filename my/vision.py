import sys
import time
from my.camera import capture_image
from my.open_vino import classify_image
from my.text_to_speech import say

def perform():
    say("Performing vision...")

    image_path = "/home/anakinz/Vision/tmp/captured_image.jpg"

    say("Capturing...")
    capture_image(image_path)

    say("Classifying...")
    classifications = classify_image(image_path)
    if classifications:
        top_classification = classifications[0]
        description = top_classification[1]
        score = top_classification[2]
        say(f"With a score of {score}, I see {description}.")
        time.sleep(1)
        say(f"I repeat, I see {description}.")
    else:
        say("Sorry, not able to classify.")

def loop():
    say("Welcome to Vision.")
    while True:
        try:
            perform()
            time.sleep(3)
        except KeyboardInterrupt:
            break

    say("Thank you for using Vision.")
    sys.exit()
