# Just Dance game made on the micro:bit. Uses gestures and radio to play. 
# A multiplayer game, the player that most closely matches the dance 
# moves of the coach wins! 
# IDE used: python.microbit.org

# Chris Lovell
# 25th October 2024
# @mrlovellcomp



# Import radio library 
from microbit import *
import radio
radio.on()
#Set radio power to 1, we are all dancing in the same room!
#Set radio channel to be the same on all micro:bits
radio.config(group=23, power=2)
#Set score to zero
score = 0

# Code in a 'while True:' loop repeats forever
while True:
    # add a small pause before checking for a message
    sleep(500)
    # store the string received by the radio into a variable named 'message'
    message = radio.receive()
    # If the micro:bit is shaken, display the score
    if accelerometer.was_gesture('shake'):
        display.show(score)
        sleep(2000)
        display.clear()
    # now broadcast on radio depending on micro:bit gesture
    # nested if will only increase score by 1 if both the broadcasting micro:bit 
    # held by the JustDance coach is being held with the same gesture as the player 
    if accelerometer.was_gesture('left'):
        radio.send('left')
        if message == 'left':
            score = score + 1
    if accelerometer.was_gesture('right'):
        radio.send('right')
        if message == 'right':
            score = score + 1
    if accelerometer.was_gesture('face up'):
        radio.send('face up')
        if message == 'face up':
            score = score + 1
    if accelerometer.was_gesture('face down'):
        radio.send('face down')
        if message == 'face down':
            score = score + 1
