keel = input("Do you want to kill or freeze the program? ")

if keel == "yes":
    keel_2 = input("Are you sure? ")
    if keel_2 == "yes":
        i = input("Enter any word: ")
        while i != "hfhfhhjfdhjhjfhjfdh":
            print(i)
    elif keel_2 == "no":
        print("Good Choice")

elif keel == "no":
    print("Ok Then!")
    print("Have a Good day.")
