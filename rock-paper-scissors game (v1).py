import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue 
        # re-sask the user_input question till user gives valid input

    randomNumber = random.randint(0, 2)
    # rock: 0  paper: 1   scissors: 2
    computerPick = options[randomNumber]
    print("Computer picked, " + computerPick)

    if user_input == "rock" and computerPick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computerPick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computerPick == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("Computer won :(")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye")