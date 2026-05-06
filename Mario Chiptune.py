# Vibe coded with Gemini 1.5 Flash
# Mario ChipTune
# Chris Lovell
# 6th May 2026

from microbit import *
import music

# 1. Hardware Setup
speaker.on()
set_volume(255)

# SECTION: Overworld Intro
intro = ['E5:2', 'E5:2', 'R:2', 'E5:2', 'R:2', 'C5:2', 'E5:2', 'R:2', 'G5:4', 'R:4', 'G4:4', 'R:4']

# SECTION: Main Theme A (The Hook)
overworld_a = [
    'C5:4', 'G4:4', 'E4:4', 'A4:4', 'B4:4', 'A#4:2', 'A4:4',
    'G4:2', 'E5:2', 'G5:2', 'A5:4', 'F5:2', 'G5:2',
    'R:2', 'E5:4', 'C5:2', 'D5:2', 'B4:4'
]

# SECTION: The Underworld (The 'Duh-duh-duh, duh-duh-duh')
underworld = [
    'C4:2', 'C5:2', 'A3:2', 'A4:2', 'A#3:2', 'A#4:2', 'R:4',
    'C4:2', 'C5:2', 'A3:2', 'A4:2', 'A#3:2', 'A#4:2', 'R:4',
    'F3:2', 'F4:2', 'D3:2', 'D4:2', 'D#3:2', 'D#4:2', 'R:4',
    'F3:2', 'F4:2', 'D3:2', 'D4:2', 'D#3:2', 'D#4:2', 'R:4'
]

# SECTION: Star Power (Fast and high)
star_power = [
    'C5:1', 'R:1', 'B4:1', 'A4:1', 'G4:1', 'R:1', 'G4:1', 'A4:1',
    'B4:1', 'R:1', 'A4:1', 'G4:1', 'F4:1', 'R:1', 'F4:1', 'G4:1'
]

# Build the 90-second "Mega Medley"
# Overworld x2 -> Underworld x2 -> Star Power x4 -> Overworld x2
mario_90s = (intro + overworld_a) * 2 + (underworld * 2) + (star_power * 8) + overworld_a

music.set_tempo(bpm=180, ticks=4)

while True:
    # Use Button A to ignite the medley
    if button_a.is_pressed():
        music.stop()
        # wait=False lets the micro:bit stay responsive
        music.play(mario_90s, wait=False)
    
    # Just a small heartbeat to keep the loop alive
    sleep(100)
