# Imports go at the top
from microbit import *
import random
microGo = []
playerGo = []
guessCount = 0
guessCorrect = 0
randomNum = 0

# Code in a 'while True:' loop repeats forever
while True:
    #If A is pressed, collect 1 and add to playerGo array
    if button_a.was_pressed():
        display.scroll('1')
        playerGo.append(1)
        #Increase guessCount variable
        guessCount = guessCount + 1
    #If B is pressed, collect 2 and add to playerGo array
    elif button_b.was_pressed():
        display.scroll('2')
        playerGo.append(2)
        #Increase guessCount variable
        guessCount = guessCount + 1
    #If A+B is pressed, collect 3 and add to playerGo array
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll('3')
        playerGo.append(3)
        #Increase guessCount variable
        guessCount = guessCount + 1
    #If shaken, have micro:bit generate a random pattern
    #and show on the LED display
    if accelerometer.was_gesture('shake'):
        for i in range(3):
            randomNum = random.randint(1,3)
            microGo.append(randomNum)
        for i in range(3):
            display.scroll(microGo[i])
    #If three guesses have been made, run the array check
    #and display well done, or try again, based on the result.
    if guessCount == 3:
        for i in range(3):
            if microGo[i] == playerGo[i]:
                guessCorrect = guessCorrect + 1
        if guessCorrect == 3:
            display.scroll("Well Done!")
        else:
            display.scroll("Try again!")
        #Now reset the variables and clear the arrays for another go
        guessCount = 0
        guessCorrect = 0
        microGo.clear()
        playerGo.clear()
