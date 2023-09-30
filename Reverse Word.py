check = input("Do you want to get the word you type Reversed(Yes or No): ")

if check.lower() == "yes":
    ask = input("Write down the Word: ")
    ask = ask[::-1]
    print("Here is your word Reversed:", ask)

elif check.lower() == "no":
    print("Ok! It was a Pleasure Meeting you.")
    print("Have a Great Day!")

else:
    print("Please give your Answer as Yes or No.")
