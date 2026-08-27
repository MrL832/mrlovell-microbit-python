
# Code repo created for Hello World "Using the micro:bit for teaching GCSE Computer Science" by Chris Lovell and available in January 2027

from microbit import *

# The secret password: a sequence of A and B presses
SECRET = ["A", "B", "B", "A"]

# What the learner has entered so far (incomplete login attempt)
entered = []

def add_press(letter):
    """Add a button press to the attempt and show it."""
    entered.append(letter)          # store it in the list
    display.show(letter.lower())    # small feedback: a or b
    sleep(400)

def check_login():
    """Compare the attempt to the secret, element by element."""
    if len(entered) != len(SECRET):
        display.show(Image.NO)
        sleep(500)
        entered.clear()             # reset the attempt
        return

    match = True
    for i in range(len(SECRET)):
        if entered[i] != SECRET[i]: # compare one position at a time
            match = False
            break

    if match:
        display.show(Image.YES)     # login succeeded
    else:
        display.show(Image.NO)      # login failed

    sleep(800)
    entered.clear()                 # reset for the next attempt

# Show the secret (for the teacher's demo) on startup
display.scroll("LOGIN")

while True:
    if button_a.was_pressed():
        add_press("A")

    if button_b.was_pressed():
        add_press("B")

    # Shake to submit the password
    if accelerometer.was_gesture("shake"):
        check_login()
