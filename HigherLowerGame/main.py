#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
import pyfiglet
print(pyfiglet.figlet_format("Higher Lower !"))
# Allow the player to submit a guess for a number between 1 and 100.
computer_choice = random.randint(0, 100)
print(f"Computer choice is {computer_choice}")
difficulty = (input("What is the difficulty you want, easy or hard? \n")).lower()
print(difficulty)

if difficulty == "hard":
    lifeline = 2
elif difficulty == "easy":
    lifeline = 10
else:
    print("Invalid Input")

PLAYER_STATUS = "playing"

def life():
    if lifeline == 0:
        global PLAYER_STATUS
        PLAYER_STATUS = "lose"
    else:
        PLAYER_STATUS = "playing"

while PLAYER_STATUS == "playing":
    player_guess = int(input("What is your guess between 0-100? \n"))
    if player_guess > computer_choice:
        print("Too High")
        lifeline -= 1
        print(f"You have {lifeline} life")
        life()
    elif player_guess < computer_choice:
        print("Too Low")
        lifeline -= 1
        print(f"You have {lifeline} life")
        life()
    else:
        PLAYER_STATUS = "win"

def game_result():
    if PLAYER_STATUS == "win":
        print("You have won")
    else:
        print("You have lost")
game_result()
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

