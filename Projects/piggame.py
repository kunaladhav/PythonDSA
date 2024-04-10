import random


def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll


value = roll()

while True:
    players = input("Enter the number of Players (2 - 5): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")

    else:
        print("Invalid. Try again")
