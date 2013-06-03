# Quick script that displays random chords from the text file "chords_bag.txt"
# Optional argment is amount of seconds between chords, Default is 4 seconds

from time import sleep
import random
import sys

try:
    sleep_seconds = int(sys.argv[1])
except IndexError:
    sleep_seconds = 3

known_chords = []

with open("chords_bag.txt", "r") as chords_list:
    for chord in chords_list:
        known_chords.append( chord.strip())

prev = random.sample(known_chords, 1)[0]        
while (True):
    curr = random.sample(known_chords, 1)[0]
    if curr != prev:
        print curr
        prev = curr
        sleep(sleep_seconds)
