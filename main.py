### the code

## Goals
# 1. Get the amount of players
# 2. Start asking for each players name and set their name and number
# 3. Wait and ask for which player's amount to set (ask in millions and convert their number into integers for proper calculations, also ask the proper format so that we can easily convert and calculate it)
# 4. Calculate the amount of money and print it out then wait for step 2 again

import time
import math

def ordinalnumbers(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

def amount_players():
    players = int(input("How many players are there? (input a number)"))
    if players < 1:
        print("Please input a number greater than 0\n")
        return amount_players()
    if type(players) is not int:
        print("Please input a number\n")
        return amount_players()
    return players

def get_player_name():
    GetPlayerName = input(f"What is the {ordinalnumbers()} player's name?")