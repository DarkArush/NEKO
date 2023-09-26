check = input("Do you want to Check Whether a Word is a Palindrome or Not(Yes or No): ")

if check.lower() == "yes" or check == "Yes":
    ask = input("Write down the Word: ")

    if ask == ask[::-1]:
        print("It's a Palindrome!")

    else:
        print("It's not a Palindrome.")

elif check.lower() == "no" or check == "No":
    print("Ok! It was a Pleasure Meeting you.")
    print("Have a Great Day!")

else:
    print("Please give your Answer as Yes or No.")
