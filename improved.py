# Author:   Austin Walters
# Language: Python 3.5.0

import sys
import time
from fractions import gcd

# Finds the lowest common multiple
def lcm(deck):
    p = 1
    for i in range(0, len(deck)):
        p = p * int(deck[i] / gcd(p, deck[i]))
    return p

# Oututs the deck after single round
def completeRound(deck):
    table = []
    while len(deck) > 0:
        table.append(deck.pop(0))        
        if len(deck) != 0:
            deck.append(deck.pop(0))
    table.reverse()
    return table

# Determines cycles between current and initial configuration
def cycles(post_round_one_deck):
    group = [1] * len(post_round_one_deck)
    for i in range(0, len(post_round_one_deck)):
        index = i
        while post_round_one_deck[index] != i:
            index = post_round_one_deck[index]
            group[i] += 1
    return group

# Generate deck from deckSize
def genDeck(deck_size):
    return list(range(0, deck_size))

# Finds number of rounds based on input deck
def findNumberOfRounds(deck):
    return lcm(cycles(completeRound(deck)))

''' ___ MAIN ___ '''
if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
    size = int(sys.argv[1])
    print('\n', size, "cards =>", findNumberOfRounds(genDeck(size)), "rounds\n")
else:
    print('\n', "Invalid, should be in the form:\n\n\t$ python solution.py (deck size > 0)\n")
