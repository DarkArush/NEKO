## asking the user whether he wants to play the game or not
user_input = input("Let's play a Game. Are you Ready? ")

## conditions: if he says yes
if user_input.lower() == "yes":
    print("Ok. Let's Play!")
    print("I will ask you 10 random questions. You have to answer in only Yes or No.")
    print("WARNING! Orphans please play at your own risk because this game might hurt you.")

    ## questions from one to four: basic informations about the user
    que_one = input("So here's the first question. What is your name? ")
    que_two = float(input("Ok, what is your age? "))
    que_three = input("What is your Gender? ")
    que_four = input("And where are you from? ")

    three = que_three

    ## details given by the user about himself/herself in the first four questions
    print("So, as per you information, Here are your Details: ")
    print("Name:", que_one, "Age:", que_two, "Gender:", que_three, "Address:", que_four)
    print("Ok. I was just making sure. Anyway, let's continue our game.")
    print("The next 5 questions will get progressively harder.")

        ## changes in question six according to the answer given by the user in question three: male
    if que_three.lower() == "male":
            que_six = input("Are you Gay? ")

        ## changes in question six according to the answer given by the user in question three: female
    elif que_three.lower() == "female":
            que_seven = input("Are you Lesbian? ")

        ## question eight: Virginity
    que_eight = input("Are you Virgin? ")

        ## question nine: Adulthood
    que_nine = input("Have you kissed someone? ")

        ## question ten: Sex
    que_ten = input("Have you slept with someone? ")

        ## xtra qustions because the above question were only nine
    xtra_que = input("WARNING! The next question might quite offend you. Do you still want to answer it? ")

        ## asking if the user wants to answer the last question: no
    if xtra_que.lower() == "no":
        print("Ok Then! Have a good day.")

        ## asking if the user wants to answer the last question: yes
    elif xtra_que.lower() == "yes":
        print("Ok. So here's the question:")

        ## Last question
        que_twelve = input("Did you Tell your parents that you like someone of ths same gender as yours?")

        ## conditions: if the last answer is yes
        if que_twelve.lower() == "yes":
             print("Yes. That's more like it")

        ## conditions: if the last answer is no
        elif que_twelve.lower() == "no":
             print("Then what are you waithing for? Go Tell Them!")

    ## credits                
    print("I hope you liked the Game!")

    ## asking for some ratings
    rating = input("Please give us some ratings on our new Game. ")

    ## greetings
    print("Thankyou for your Rating. I hope you Enjoyed our Game.")
    print("So, Goodbye.")

## conditions: if he says no
elif user_input.lower() == "no":
    print("Ok Then! Have a Good Day.")

## conditions: if he gives answers other than yes or no
else:
    print("Please give your answer in Yes or No.")
