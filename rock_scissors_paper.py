import random
import time

class Player:
    def __init__(self, name, selection=None, score=0):
        self.name = name
        self.selection = selection
        self.score = score

def game():
    options = ("ROCK", "SCISSORS", "PAPER")
    shift_AI = Player("Shift")
    player = Player(input("\nEnter your name: "))

    while True:
        try:
            rounds = int(input("\nHow may rounds? (1-21): "))
            if rounds < 1 or rounds > 21:
                print("\nInvalid value")
                time.sleep(2)
            else:
                break
        except ValueError:
            print("\nOnly numbers are allowed")
            time.sleep(2)
    
    for count in range (0, rounds):
        while True:
            valid_option = False
            print(f"\nRound {count+1}/{rounds}")
            print("\nROCK,")
            time.sleep(1)
            print("SCISSORS,")
            time.sleep(1)
            print("PAPER")
            time.sleep(1)
            player.selection = input("\nCHOOSE: ").upper()
            for i in range (0, len(options)):
                if options[i] == player.selection:
                    valid_option = True
                    break
            if valid_option == True:
                break
            else:    
                print("\nEnter a valid option")
                time.sleep(3)
        
        shift_AI.selection = options[random.randint(0, (len(options) - 1))]
        announcement1 = f"\n{player.name}: {player.selection}"
        announcement2 = f"{shift_AI.name}: {shift_AI.selection}"

        #Rock Rules
        if player.selection.upper() == "ROCK" and shift_AI.selection == "ROCK":
            print(f"{announcement1}     |     {announcement2}\n\nDRAW")
        elif player.selection.upper() == "ROCK" and shift_AI.selection == "SCISSORS":
            print(f"{announcement1}     |     {announcement2}\n\nVictory")
            player.score += 1
        elif player.selection.upper() == "ROCK" and shift_AI.selection == "PAPER":
            print(f"{announcement1}     |     {announcement2}\n\nDefeat")
            shift_AI.score += 1

        #Scissors Rules
        elif player.selection.upper() == "SCISSORS" and shift_AI.selection == "ROCK":
            print(f"{announcement1}     |     {announcement2}\n\nDefeat")
            shift_AI.score += 1
        elif player.selection.upper() == "SCISSORS" and shift_AI.selection == "SCISSORS":
            print(f"{announcement1}     |     {announcement2}\n\nDRAW")
        elif player.selection.upper() == "SCISSORS" and shift_AI.selection == "PAPER":
            print(f"{announcement1}     |     {announcement2}\n\nVictory")
            player.score += 1

        #Paper Rules
        elif player.selection.upper() == "PAPER" and shift_AI.selection == "ROCK":
            print(f"{announcement1}     |     {announcement2}\n\nVictory")
            player.score += 1
        elif player.selection.upper() == "PAPER" and shift_AI.selection == "SCISSORS":
            print(f"{announcement1}     |     {announcement2}\n\nDefeat")
            shift_AI.score += 1
        else:
            print(f"{announcement1}     |     {announcement2}\nDRAW")
        time.sleep(2)
        print(f"\nResults: \n{player.name} = {player.score}\n{shift_AI.name} = {shift_AI.score}")

    if player.score > shift_AI.score:
        print(f"\nWinner: {player.name}\n")
    elif player.score < shift_AI.score:
        print(f"\nWinner {shift_AI.name}\n")
    else:
        print("\nDRAW\n")

    
def main():
    game()

if __name__ == "__main__":
    main()