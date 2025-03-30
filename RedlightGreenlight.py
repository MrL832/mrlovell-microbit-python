# Red light, Green light
# A game on the micro:bit inspired by the game 'grandma's footsteps & red light, green light.
# Game uses the micro:bit's radio to broadcast to a class size number (30+) 
# of micro:bits on the same radio group
# when button 'A' is pressed on a lead micro:bit
# Micro:bit plays an annoucement and shows an 'X' when a message is received
# 
# Created by Chris Lovell 30th March 2025

from microbit import *
import radio
import music
radio.config(group=23)


# Code in a 'while True:' loop repeats forever
while True:
    radio.on()
    while True:
        radio.on()
        message = radio.receive()
        sleep(400)
        if button_a.is_pressed():
            radio.send('Stop!')
        if message:
            music.play(music.BA_DING)
            display.show(Image.NO)
        else:
            display.show(Image.ARROW_N)
