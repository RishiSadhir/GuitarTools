
# Simple script to help me learn the notes on a fret board
# Flashes a string and a fret number -- Guess the Note

from time import sleep
import random
import sys

try:
    sleep_seconds = int(sys.argv[1])
except IndexError:
    sleep_seconds = 5

strings = ['E_low', 'A', 'D', 'G', "B", "E_hi"]
frets = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
notecache = {}

notecache["E_low1"]  = "F" 
notecache["E_low2"]  = "F#"
notecache["E_low3"]  = "G" 
notecache["E_low4"]  = "G#"
notecache["E_low5"]  = "A" 
notecache["E_low6"]  = "A#"
notecache["E_low7"]  = "B" 
notecache["E_low8"]  = "C" 
notecache["E_low9"]  = "C#"
notecache["E_low10"] = "D"
notecache["E_low11"] = "D#"
notecache["E_low12"] = "E"
notecache["A1"]      = "A#"
notecache["A2"]      = "B"
notecache["A3"]      = "C"
notecache["A4"]      = "C#"
notecache["A5"]      = "D"
notecache["A6"]      = "D#"
notecache["A7"]      = "E"
notecache["A8"]      = "F"
notecache["A9"]      = "F#"
notecache["A10"]     = "G"
notecache["A11"]     = "G#"
notecache["A12"]     = "A"
notecache["D1"]      = "D#"
notecache["D2"]      = "E"
notecache["D3"]      = "F"
notecache["D4"]      = "F#"
notecache["D5"]      = "G"
notecache["D6"]      = "G#"
notecache["D7"]      = "A"
notecache["D8"]      = "A#"
notecache["D9"]      = "B"
notecache["D10"]     = "C"
notecache["D11"]     = "C#"
notecache["D12"]     = "D"
notecache["G1"]      = "G#"
notecache["G2"]      = "A"
notecache["G3"]      = "A#"
notecache["G4"]      = "B"
notecache["G5"]      = "C"
notecache["G6"]      = "C#"
notecache["G7"]      = "D"
notecache["G8"]      = "D#"
notecache["G9"]      = "E"
notecache["G10"]     = "F"
notecache["G11"]     = "F#"
notecache["G12"]     = "G"
notecache["B1"]      = "C"
notecache["B2"]      = "C#"
notecache["B3"]      = "D"
notecache["B4"]      = "D#"
notecache["B5"]      = "E"
notecache["B6"]      = "F"
notecache["B7"]      = "F#"
notecache["B8"]      = "G"
notecache["B9"]      = "G#"
notecache["B10"]     = "A"
notecache["B11"]     = "A#"
notecache["B12"]     = "B"
notecache["E_hi1"]   = "F" 
notecache["E_hi2"]   = "F#"
notecache["E_hi3"]   = "G" 
notecache["E_hi4"]   = "G#"
notecache["E_hi5"]   = "A" 
notecache["E_hi6"]   = "A#"
notecache["E_hi7"]   = "B" 
notecache["E_hi8"]   =  "C" 
notecache["E_hi9"]   = "C#"
notecache["E_hi10"]  = "D"
notecache["E_hi11"]  = "D#"
notecache["E_hi12"]  = "E"

prev_string = random.sample(strings,1)[0]
prev_fret = random.sample(frets,1)[0]
while True:
    curr_string = random.sample(strings,1)[0]
    curr_fret = random.sample(frets,1)[0]
    if prev_fret == curr_fret and prev_string == curr_string:
        continue
    sys.stdout.write("String : " + curr_string + " , Fret : " + curr_fret + "   ...   ")
    sys.stdout.flush()
    sleep(sleep_seconds)
    sys.stdout.write(notecache[curr_string+curr_fret] + "\n")
    prev_string = curr_string
    prev_fret = curr_fret
    
