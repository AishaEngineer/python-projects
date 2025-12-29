import random

players = ["Player 1", "Player 2"]
positions = {"Player 1": 0, "Player 2": 0}

def roll_dice():
    return random.randint(1, 6)

print("Welcome to Simple Ludo Game")

while True:
    for player in players:
        input(f"{player}, press Enter to roll the dice...")
        dice = roll_dice()
        print(f"{player} rolled a {dice}")

        positions[player] += dice
        print(f"{player} position: {positions[player]}")

        if positions[player] >= 30:
            print(f"{player} wins!")
            exit()
