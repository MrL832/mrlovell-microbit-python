# Imports go at the top
from microbit import *
import random
tamagotchiScore = 0
playerScore = 0


# Code in a 'while True:' loop repeats forever
while True:
    display.scroll('Guess A or B')
    guess = random.randint(1,2)
    if button_a.was_pressed():
        display.scroll('You pressed A')
        if guess == 1:
            playerScore = playerScore + 1
            display.scroll(':(')
        else:
            tamagotchiScore = tamagotchiScore + 1
            display.scroll(':)')
    if button_b.was_pressed():
        display.scroll('You pressed B')
        if guess == 1:
            playerScore = playerScore + 1
            display.scroll(':(')
        else:
            tamagotchiScore = tamagotchiScore + 1
            display.scroll(':)')
    if playerScore == 3:
        display.scroll('You Win!')
    if tamagotchiScore == 3:
        display.scroll('I win!')
