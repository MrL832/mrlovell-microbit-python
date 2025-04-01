# Game made in vibe code session with google gemini v 2.0 flash 
# Game creates a random grid of LEDs. Purpose of game is to make
# all LEDs turn off. To turn them to the opposite condition LEDs press A+B
# Chris Lovell
# 1st April 2025

from microbit import *
import random

# Initialize the grid (5x5 LED matrix)
grid = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
cursor_x = 2  # Start in the center
cursor_y = 2  # Start in the center

def toggle(x, y):
    """Toggles the LED at (x, y) and its neighbors."""
    if 0 <= x < 5 and 0 <= y < 5:
        grid[y][x] = 1 - grid[y][x]  # Toggle the LED

def toggle_neighbors(x, y):
    """Toggles the LED at (x, y) and its neighbors."""
    toggle(x, y)
    toggle(x + 1, y)
    toggle(x - 1, y)
    toggle(x, y + 1)
    toggle(x, y - 1)

def draw_grid():
    """Displays the grid on the LED matrix."""
    display.clear()
    for y in range(5):
        for x in range(5):
            if grid[y][x] == 1:
                display.set_pixel(x, y, 9)
    display.set_pixel(cursor_x, cursor_y, 5) # show cursor

def check_win():
    """Checks if all LEDs are off."""
    for row in grid:
        if sum(row) > 0:
            return False
    return True

def game_loop():
    global cursor_x, cursor_y
    while True:
        draw_grid()

        x_accel = accelerometer.get_x()
        y_accel = accelerometer.get_y()

        if x_accel < -500:
            cursor_x = max(0, cursor_x - 1)
            sleep(150)
        elif x_accel > 500:
            cursor_x = min(4, cursor_x + 1)
            sleep(150)

        if y_accel < -500:
            cursor_y = max(0, cursor_y - 1)
            sleep(150)
        elif y_accel > 500:
            cursor_y = min(4, cursor_y + 1)
            sleep(150)

        if button_a.is_pressed() and button_b.is_pressed(): #Toggle with both buttons.
            toggle_neighbors(cursor_x, cursor_y)
            sleep(200)

        if check_win():
            display.show(Image.HAPPY)
            sleep(2000)
            break

        sleep(50)

game_loop()
