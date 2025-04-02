# Code created together with Google Gemini Flash 2.0 
# on 2nd April 2025
# Use A and B to move tetriminos 
# left and right, A + B together to rotate 
# clockwise. Shake to show score.


from microbit import *
import random
import music

# Game constants
GRID_WIDTH = 5
GRID_HEIGHT = 5
TICK_INTERVAL = 500  # Milliseconds between block drops

# Tetromino shapes (represented as lists of (dx, dy) offsets from the center)
TETROMINOS = [
    [(0, 0), (-1, 0), (1, 0), (0, -1)],  # T
    [(0, 0), (-1, 0), (1, 0), (2, 0)],  # I
    [(0, 0), (-1, 0), (0, -1), (1, -1)],  # S
    [(0, 0), (1, 0), (0, -1), (-1, -1)],  # Z
    [(0, 0), (-1, 0), (1, 0), (1, -1)],  # L
    [(0, 0), (-1, 0), (1, 0), (-1, -1)],  # J
    [(0, 0), (-1, 0), (0, -1), (-1, -1)]   # O
]

TETROMINO_COLORS = [9, 5, 7, 3, 6, 2, 8]  # Brightness levels

# Tetris theme music (Korobeiniki) - simplified for micro:bit
TETRIS_THEME = [
    'E5:4', 'B4:4', 'C5:4', 'D5:4', 'C5:4', 'B4:4', 'A4:4', 'A4:8',
    'F5:4', 'D5:4', 'E5:4', 'F5:4', 'E5:4', 'D5:4', 'C5:4', 'C5:8',
    'G5:4', 'E5:4', 'F5:4', 'G5:4', 'F5:4', 'E5:4', 'D5:4', 'D5:8',
    'B4:4', 'G4:4', 'A4:4', 'B4:4', 'A4:4', 'G4:4', 'E4:4', 'E4:8',
    'C5:4', 'G4:4', 'D5:4', 'E5:4', 'F5:8',
    'F5:4', 'D5:4', 'E5:4', 'F5:4', 'E5:4', 'D5:4', 'C5:4', 'C5:8',
    'G5:4', 'E5:4', 'F5:4', 'G5:4', 'F5:4', 'E5:4', 'D5:4', 'D5:8',
    'B4:4', 'G4:4', 'A4:4', 'B4:4', 'A4:4', 'G4:4', 'E4:4', 'E4:8'
]

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - 1  # Initial horizontal position
        self.y = 0  # Initial vertical position

    def get_pixels(self):
        """Returns a list of (x, y) coordinates for the current tetromino."""
        pixels = []
        for dx, dy in self.shape:
            px = self.x + dx
            py = self.y + dy
            if 0 <= px < GRID_WIDTH and 0 <= py < GRID_HEIGHT:
                pixels.append((px, py))
        return pixels

    def move(self, dx, dy, board):
        """Moves the tetromino by dx, dy if the new position is valid."""
        new_x = self.x + dx
        new_y = self.y + dy
        new_pixels = []
        for ox, oy in self.shape:
            px = new_x + ox
            py = new_y + oy
            if not (0 <= px < GRID_WIDTH and 0 <= py < GRID_HEIGHT and board[py][px] is None):
                return False  # Invalid move
            new_pixels.append((px, py))
        self.x = new_x
        self.y = new_y
        return True

    def rotate(self, board):
        """Rotates the tetromino clockwise if the new position is valid."""
        new_shape = []
        for dx, dy in self.shape:
            new_shape.append((-dy, dx))  # Clockwise rotation formula

        new_pixels = []
        for ox, oy in new_shape:
            px = self.x + ox
            py = self.y + oy
            if not (0 <= px < GRID_WIDTH and 0 <= py < GRID_HEIGHT and board[py][px] is None):
                return False  # Invalid rotation
            new_pixels.append((px, py))

        self.shape = new_shape
        return True

def create_board():
    """Creates an empty game board."""
    return [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_board(board, current_tetromino=None):
    """Displays the board and the current tetromino on the micro:bit display."""
    display.clear()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if board[y][x] is not None:
                display.set_pixel(x, y, board[y][x])
    if current_tetromino:
        for px, py in current_tetromino.get_pixels():
            display.set_pixel(px, py, current_tetromino.color)

def check_collision(tetromino, board):
    """Checks if the tetromino collides with the board or the bottom."""
    for px, py in tetromino.get_pixels():
        if py >= GRID_HEIGHT or board[py][px] is not None:
            return True
    return False

def add_tetromino_to_board(tetromino, board):
    """Adds the landed tetromino to the game board."""
    for px, py in tetromino.get_pixels():
        if 0 <= py < GRID_HEIGHT and 0 <= px < GRID_WIDTH:
            board[py][px] = tetromino.color

def clear_lines(board):
    """Clears any completed horizontal lines on the board."""
    lines_cleared = 0
    new_board = []
    for row in reversed(board):
        if all(cell is not None for cell in row):
            lines_cleared += 1
        else:
            new_board.insert(0, row)  # Add non-full rows to the top
    for _ in range(lines_cleared):
        new_board.insert(0, [None] * GRID_WIDTH)  # Add empty rows at the top
    return new_board, lines_cleared

def game_over():
    """Indicates game over on the display."""
    display.show(Image.SAD)
    music.stop()  # Stop the music on game over
    sleep(2000)

def display_score(score):
    """Displays the score on the micro:bit."""
    display.scroll("Score: {}".format(score))
    sleep(1000)  # Show score for a bit

def main():
    board = create_board()
    current_tetromino = None
    score = 0
    tick_timer = running_time()
    game_active = True
    score_displayed = False  # Flag to prevent repeated score display

    music.play(TETRIS_THEME, loop=True, wait=False) # Start background music

    while game_active:
        if current_tetromino is None:
            shape = random.choice(TETROMINOS)
            color = random.choice(TETROMINO_COLORS)
            current_tetromino = Tetromino(shape, color)
            if check_collision(current_tetromino, board):
                game_over()
                game_active = False
                continue

        # Handle user input
        if button_a.is_pressed() and not button_b.is_pressed():
            current_tetromino.move(-1, 0, board)
            sleep(100)
        elif button_b.is_pressed() and not button_a.is_pressed():
            current_tetromino.move(1, 0, board)
            sleep(100)
        elif button_a.is_pressed() and button_b.is_pressed():
            current_tetromino.rotate(board)
            sleep(200)

        # Block falling logic
        if running_time() - tick_timer >= TICK_INTERVAL:
            tick_timer = running_time()
            if not current_tetromino.move(0, 1, board):
                # Collision with the bottom or other blocks
                add_tetromino_to_board(current_tetromino, board)
                board, lines = clear_lines(board)
                score += lines * 100
                current_tetromino = None

        # Check for shake to display score
        if accelerometer.was_gesture('shake') and not score_displayed:
            display_score(score)
            score_displayed = True
            sleep(500) # Debounce the shake
        elif not accelerometer.is_gesture('shake'):
            score_displayed = False # Reset the flag when not shaking

        draw_board(board, current_tetromino)
        sleep(50)

    # Display final score after game over
    display_score(score)

if __name__ == "__main__":
    main()
