
# 28th April 2025
# Bubble Sort on the micro:bit
# This is a fun project for students learning python
# Have them code a bubble sort on a micro:bit
# The code works by comparing the contents of neighbouring 
# items in an array
# The micro:bit displays the contents of the array 
# until it is sorted


from microbit import *
import time

my_list = [8, 5, 6, 2, 1]
list_length = len(my_list)
swapped = True
# Code in a 'while True:' loop repeats forever
while swapped == True:
    sleep(500)
    swapped = False
    for i in range(list_length - 1):
        if my_list[i] > my_list[i + 1]:
            # Use a temporary variable to swap
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
            swapped = True
            display.scroll(" ")
            time.sleep(1)
            string_list = [str(item) for item in my_list]
            full_string = " ".join(string_list)
            display.show(full_string)
            time.sleep(1)

string_list = [str(item) for item in my_list]
full_string = " ".join(string_list)
display.show(full_string)
