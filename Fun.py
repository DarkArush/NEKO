check = input("Do you want to get the word you type Reversed(Yes or No): ")

if check.lower() == "yes":
    ask = int(input("""How Many Letters Would you want your Word to Contain: 
                       1. 3 Letters
                       2. 5 Letters
                       3. 7 Letters
                       4. 9 Letters
                       Choose your Option by Typing the Number Here: """))

    if ask == 1:
        name = input("Enter any Three Letter Word: ")
        name = name[::-1]
        print(name)
        if len(name) != 3:
            print("Please Enter a Three Letter Word.")

    elif ask == 2:
        name = input("Enter any Five Letter Word: ")
        name = name[::-1]
        print(name)
        if len(name) != 5:
            print("Please Enter a Five Letter Word.")

    elif ask == 3:
        name = input("Enter any Seven Letter Word: ")
        name = name[::-1]
        print(name)
        if len(name) != 7:
            print("Please Enter a Seven Letter Word.")

    elif ask == 4:
        name = input("Enter any Nine Letter Word: ")
        name = name[::-1]
        print("It's a Palindrome!")
        if len(name) != 9:
            print("Please Enter a Nine Letter Word.")

        else:
            print("Please give your answer from the options given below.")

elif check.lower() == "no":
    print("Ok! It was a Pleasure Meeting you.")
    print("Have a Great Day!")

else:
    print("Please give your Answer as Yes or No.")
    print("Please give your Answer as Yes or No.")
