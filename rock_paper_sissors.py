import random 

while True:
    user = input("pick a choice (rock/paper/sissors)")
    possible_actions= ["rock","paper","sissors"]
    computer_action = random.choice(possible_actions)
    if user == computer_action:
        print("It's a tie")
    elif user == "rock":
        if computer_action == "paper":
            print("You paper cover rock. YOU LOSE ")
        else:
            print("rock smashes sissors.YOU WIN")

    elif user == "paper":
        if computer_action == "sissors":
            print("You paper gets cut. YOU LOSE ")
        else:
            print("rock is now covered.YOU WIN")

    elif user == "sissors":
        if computer_action == "rock":
            print("You rock breakes sissors. YOU LOSE ")
        else:
            print("rock smashes sissors.YOU WIN")

    play= input("Do you want to play yes or no?(y/n)")
    if play == "n":
        break
