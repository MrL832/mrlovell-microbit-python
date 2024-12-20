# A simple number guessing game
# Aim is for the player to guess whether their 
# randomly generated number is higher or lower than the 
# number randomly generated by the micro: bit
# Created by Chris Lovell on 31st October 2024
# Find @mrlovellcomp



#imports including random 
from microbit import *
import random
mbNumber = 0
score = 0


# Game will repeat. Aim to have have several players, playing several rounds
# Player with the highest score wins
while True:
    # Randomly generate a number that the microbit holds
    mbNumber = random.randint(1,10)
    # Randomly generate a number for the player
    playerNumber = random.randint(1,10)
    display.scroll(mbNumber)
    sleep(2000)
    # Simple message asking the player to guess higher or lower
    display.scroll("?")
    # Nested selection to check whether the micro:bit number is higher or lower than the player's
    if button_a.was_pressed():
        if playerNumber > mbNumber:
            display.scroll('W')
            score = score + 1
        else:
            display.scroll('L')
    if button_b.was_pressed():
        if playerNumber < mbNumber:
            display.scroll('W')
            score = score + 1
        else:
            display.scroll('L')
    # Shake the micro:bit to show the player score. 
    if accelerometer.was_gesture('shake'):
        display.scroll(score)
