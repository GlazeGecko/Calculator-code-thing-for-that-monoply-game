### the code

## Goals
# 1. Get the amount of players
# 2. Start asking for each players name and set their name and number
# 3. Wait and ask for which player's amount to set (ask in millions and convert their number into integers for proper calculations, also ask the proper format so that we can easily convert and calculate it)
# 4. Calculate the amount of money and print it out then wait for step 2 again

import time
import math

# Variables
value = []
e = 0

print("Welcome to the Money Calculator\n")
# Functions
def ordinalnumbers(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

def amount_players():
    try:
        players = int(input("How many players are there? (input a number) "))
        if players < 1:
            print("Please input a number greater than 0\n")
            return amount_players()
        if players > 10:
            print("Please input a number less than 10\n")
            return amount_players()
        return players
    except ValueError:
        print("Please input a number\n")
        return amount_players()
amount_players = amount_players()

def get_player_name():
    player_names = []
    for i in range(amount_players):
        i += 1
        player_name = input(f"What is the {ordinalnumbers(i)} player's name? ")
        player_names.append(player_name)
    return player_names

players = get_player_name()
print(players)

def value_for_player():
    player_values = []
    for i in range(amount_players):
        while True:
            try:
                value = input(f"Set the amount of money for '{players[i]}': ")
                value = float(value.replace(",", "").replace("$", "").replace(" ", ""))
                player_values.append(value)
                break
            except ValueError:
                print("Please input a number\n")
                continue
    return player_values
player_values = value_for_player() # should be a list
print(player_values)
formatted_values = [f"{value:,.2f}" for value in player_values]
formatted_values = [f"${value}" for value in formatted_values]
for i in range(amount_players):
    print(f"{players[i]} has {formatted_values[i]}")
def calculate_amount():
    player_calculate = input("Which player's amount do you want to calculate?")
    

    return players[e]
calculate_amount()