import random
import os
import tkinter


deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()

        if card == 11: card = "j"
        if card == 12: card = "q"
        if card == 13: card = "k"
        if card == 14: card = "A"

        hand.append(card)
    return hand

print(deck)