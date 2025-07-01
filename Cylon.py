# A "cylon eye" effect on the micro:bit just for fun
# Chris Lovell 1st July 2025

# Imports go at the top
from microbit import *

def cylon_eye():
    for i in range(5):
        display.set_pixel(i, 2, 9)
        sleep(70)
        if i > 0:
            display.set_pixel(i-1, 2, 0)
    for i in range(3, -1, -1):
        display.set_pixel(i, 2, 9)
        sleep(70)
        if i < 4:
            display.set_pixel(i+1, 2, 0)
    display.clear() # Clear after effect

# Code in a 'while True:' loop repeats forever
while True:
    cylon_eye()
