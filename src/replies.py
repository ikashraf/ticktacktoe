from itertools import chain
from random import choice

def bot_reply(X_positions, O_positions):
    avaiable_positions = {1,2,3,4,5,6,7,8,9}
    for position in chain(X_positions, O_positions):
        avaiable_positions.remove(position)

    return choice(list(avaiable_positions))

def player_reply(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("not an integer")
    return value  