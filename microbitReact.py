#micro:bit React Game 
#Created by Chris Lovell
# 24th October 2024
# This is a two-player game, where each player is assigned to the A or B button. The players listen for a sound and first to press their button wins!

# Imports go at the top
from microbit import *
import music
import random


# Code in a 'while True:' loop repeats forever
while True:
    sleep(1000)
    #Show a target on the display
    display.show(Image.TARGET)
    sleep(400)
    #Shake to start
    if accelerometer.was_gesture('shake'):
        #show a '3,2,1' countdown
        display.show(3)
        sleep(1000)
        display.show(2)
        sleep(1000)
        display.show(1)
        sleep(1000)
        #Delay the buzzer for a random moment of time
        wait = random.randint(1, 3)
        if wait == 1:
            sleep(1000)
        elif wait == 2:
            sleep(2000)
        else:
            sleep(500)
        #Increase sound volume to the loudest
        set_volume(255)
        #Play a starter note
        music.play(['c'])
        #Use 'is pressed' to detect who presses the button first
        if button_a.is_pressed():
            display.scroll('A!')
        if button_b.is_pressed():
            display.scroll('B!')
        
