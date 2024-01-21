# v1
import random

while True:

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Choose "rock", "paper" or "scissors": ').lower()
    if player == computer:
        print('Player:', player)
        print('Computer:', computer)
        print('Tie')
    elif player == 'rock':
        if computer == 'paper':
            print('Player:', player)
            print('Computer:', computer)
            print('Lose')
        if computer == 'scissors':
            print('Player:', player)
            print('Computer:', computer)
            print('Win')
    elif player == 'scissors':
        if computer == 'rock':
            print('Player:', player)
            print('Computer:', computer)
            print('Lose')
        if computer == 'paper':
            print('Player:', player)
            print('Computer:', computer)
            print('Win')
    elif player == 'paper':
        if computer == 'scissors':
            print('Player:', player)
            print('Computer:', computer)
            print('Lose')
        if computer == 'rock':
            print('Player:', player)
            print('Computer:', computer)
            print('Win')
    play_again = input('Play again? (yes[y]/no[n])').lower()

    if play_again != 'yes' and play_again != 'y':
        break
print('Thank you for playing!\nBye')

# v2
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    exit("Invalid Input. Try again...")

npc_random_num = random.randint(1, 3)
npc_move = ""

while True:
    if npc_random_num == 1:
        npc_move = rock
    elif npc_random_num == 2:
        npc_move = paper
    elif npc_random_num == 3:
        npc_move = scissors

    if (player_move == rock and npc_move == scissors) or \
            (player_move == paper and npc_move == rock) or \
            (player_move == scissors and npc_move == paper):
        print(f"You choose: {player_move}\nComputer choose: {npc_move}")
        print("You win!")
    elif (player_move == scissors and npc_move == rock) or \
            (player_move == rock and npc_move == paper) or \
            (player_move == paper and player_move == scissors):
        print(f"You choose: {player_move}\nComputer choose: {npc_move}")
        print("You lose!")
    else:
        print(f"You choose: {player_move}\nComputer choose: {npc_move}")
        print("Tie!")

    play_once_again = input("Type 'yes/y' to Play Again or 'no/n' to quit: ").lower()
    if play_once_again == "yes" or play_once_again == "y":
        continue
    else:
        print("Thank you for playing!\nBye")
        break
