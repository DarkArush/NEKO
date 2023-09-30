import random

spr = input("Do you want to play rock paper scissors? ")

if spr == "yes":
    print("Ok! Let's play.")
    choice = input("Play your move: ")
    if choice in ["rock", "paper", "scissor"]:
        computer_choice = random.choice(["rock", "paper", "scissor"])
        print(computer_choice)
        if choice == "rock" and computer_choice == "paper":
            print("I Won!")
        elif choice == "rock" and computer_choice == "scissor":
            print("You Won.")
        elif choice == "paper" and computer_choice == "scissor":
            print("I Won!")
        elif choice == "paper" and computer_choice == "rock":
            print("You Won.")
        elif choice == "scissor" and computer_choice == "rock":
            print("I Won!")
        elif choice == "scissor" and computer_choice == "paper":
            print("You Won.")
        elif choice == computer_choice:
            print("It's a Draw.")
        print("Good Game.")

elif spr == "no":
    print("Ok Then!")
    print("Have a Good Day.")

else:
    print("Please Tell me in only Yes or No.")