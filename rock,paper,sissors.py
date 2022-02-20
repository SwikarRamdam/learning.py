import random

while True:
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    print("Welcome to GuessMe !")
    player = None
    computer = random.choice(choices) #choices will produce output in []
# player = input("Guess the output: Rock, Paper or Scissors\n")
    while player not in choices:
        player = input("Guess the output: Rock, Paper or Scissors\n")
        # player = player.upper() why the case changing brings error and runs loop again and again remains a mystery

    print("Your answer = ",player)
    print("Computer answer = ",computer)
# if(player==computer):
#     print("You guessed it right ! \n It is ",computer)
# else:
#     print("Try again !")
    if player==computer:
        print("Tie !")
    elif player=="Rock":
        if computer=="Scissors":
            print("You win !")
        elif computer=="Paper":
            print("You lose !")
    elif player=="Scissors":
        if computer=="Paper":
            print("You win !")
        elif computer=="Rock":
            print("You lose !")
    elif player=="Paper":
        if computer=="Rock":
            print("You win !")
        elif computer=="Scissors":
            print("You lose !")
    
    play_again = input("Play Again (yes/no)?").lower()

    if play_again!="yes":
        break
print("Thank You !")
