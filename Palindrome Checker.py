check = input("Do you want to Check Whether a Word is a Palindrome or Not(Yes or No): ")

if check.lower() == "yes" or check == "Yes":
    ask = int(input("""How Many Letters Would you want your Word to Contain: 
                       1. 3 Letters
                       2. 5 Letters
                       3. 7 Letters
                       4. 9 Letters
                       Choose your Option by Typing the Number Here: """))

    if ask == 1:
        name = input("Enter any Three Letter Word: ")
        if name[0] == name[2]:
            print("It's a Palindrome!")
        elif ask.bit_length() < 3 or ask.bit_length() > 3:
            print("PLease Enter a Three Letter Word.")

    elif ask == 2:
        name = input("Enter any Five Letter Word: ")
        if name[0] == name[4] and name[1] == name[3]:
            print("It's a Palindrome!")
        elif ask.bit_length() < 5 or ask.bit_length() > 5:
            print("PLease Enter a Three Letter Word.")

    elif ask == 3:
        name = input("Enter any Seven Letter Word: ")
        if name[0] == name[6] and name[1] == name[5] and name[2] == name[4]:
            print("It's a Palindrome!")
        elif ask.bit_length() < 7 or ask.bit_length() > 7:
            print("PLease Enter a Three Letter Word.")

    elif ask == 4:
        name = input("Enter any Nine Letter Word: ")
        if name[0] == name[8] and name[1] == name[7] and name[2] == name[6] and name[3] == name[5]:
            print("It's a Palindrome!")
        elif ask.bit_length() < 9 or ask.bit_length() > 9:
            print("PLease Enter a Three Letter Word.")

        else:
            print("It's not a Palindrome.")

elif check.lower() == "no" or check == "No":
    print("Ok! It was a Pleasure Meeting you.")
    print("Have a Great Day!")

else:
    print("Please give your Answer as Yes or No.")
