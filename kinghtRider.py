# Knight Rider LED Scan for micro:bit
# This script creates the iconic Knight Rider style LED animation
# on the micro:bit's display, moving back and forth across the middle row.

from microbit import *

# Function to perform one sweep of the Knight Rider LED scan
# The 'brightness' parameter controls how bright the LED is (0-9)
# The 'delay_ms' parameter controls the speed of the scan in milliseconds
def knight_rider_led_scan_sweep(brightness=9, delay_ms=50):
    # Scan from left to right across the middle row (row 2)
    for x in range(5): # Columns 0, 1, 2, 3, 4
        display.clear() # Clear previous LED
        display.set_pixel(x, 2, brightness) # Light up pixel at (x, row 2)
        sleep(delay_ms)
    # Scan from right to left (excluding the end points to create a smooth bounce)
    # Starts from column 3 down to 1 (0 is handled by the first loop's start)
    for x in range(3, 0, -1): # Columns 3, 2, 1
        display.clear() # Clear previous LED
        display.set_pixel(x, 2, brightness)
        sleep(delay_ms)
    display.clear() # Ensure display is clear at the end of a single sweep

# Main loop to continuously play the Knight Rider LED scan
while True:
    display.show(Image.TARGET) # Show a target icon or similar to indicate activity
    # Perform the LED scan animation.
    # A single LED sweep takes (5 + 3) * 50ms = 400ms.
    # You can adjust the number of sweeps or the delay_ms for different speeds.
    for _ in range(5): # Run the LED scan 5 times per cycle
        knight_rider_led_scan_sweep(brightness=9, delay_ms=50)

    display.clear() # Ensure display is clear before the next cycle begins
    sleep(200) # Short pause before repeating the entire LED scan sequence
