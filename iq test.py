import random
import time
from colorama import Fore

ask = input("Do you want to take an IQ test?")
while ask != "no":
    time.sleep(1)
    print(Fore.CYAN + "I will ask you 5 questions.")
    time.sleep(1)
    print(Fore.CYAN + "Starting from beginner question to expert level question.")
    time.sleep(1)
    print(Fore.CYAN + "Let's start!")
    print(Fore.GREEN + "_"*60)

    player_score = 0

    print(Fore.RED + "These two questions will be of beginner level.")
    time.sleep(1)
    print(Fore.RED + "Please type the correct option and not the answer.")

    time.sleep(1)
    print(Fore.CYAN + "First Question:")
    first_que = [Fore.YELLOW + """What is 49 percent of 90?
                        A) 44.1
                        B) 36.8
                        C) 50.4
                        D) 69
                 ""","""A piece of cloth costs 35$. If the price were 4m longer and each metre costs 1$ less, the cost would remain unchanged. How long is the price?
                    A) 10m
                    B) 12m
                    C) 15m
                    D) 13.8m
                    ""","""A dealer sells an article for 24$ and gains as much percent as the cost price of the article. Find the cost price of the article.
                    A) 20$
                    B) 16$
                    C) 25$
                    D) 37$
                    """]

    que1 =  input(random.choice(first_que))
    print(que1)
    if que1.upper() == "A":
        player_score =+ 1
    else:
        player_score =- 1
    time.sleep(1)
    print((Fore.MAGENTA + "Processing Answer"))
    time.sleep(1)

    print(Fore.YELLOW + "Second Question:")
    second_que = ["""What will come next in the series: 1, 4, 9, 16, ?
                  A) 64
                  B) 81
                  C) 36
                  D) 25
               ""","""If two paralle lines touch a circle at two points P and Q and the area of the circle is 25pie cm^2, find the distance PQ.
                    A) 25cm
                    B) 5cm
                    C) 15cm
                    D) 10cm
                    ""","""A train covers a distance of 90km at a uniform speed. Had the speed been 15km/hour more, it would have taken 30 minutes less for the journey. Find the original speed of the train.
                            A) 30km/hr
                            B) 60km/hr
                            C) 90km/hr
                            D) 45km/hr
                            """]
    
    que2 = input(random.choice(second_que))
    print(que2)
    if que2.upper() == "D":
        player_score += 1
    else:
        player_score -= 1

    time.sleep(1)
    print((Fore.MAGENTA + "Processing Answer"))
    time.sleep(1)
    print("_"*60)

    print(Fore.RED + "These questions are of intermediate level.")

    third_que = [Fore.YELLOW + """In a lake, there is a patch of lily pads. Every day, the patch doubles in size.If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?
                                  A) 15
                                  B) 24
                                  C) 47
                                  D) 48 
                                  ""","""At the end of a banquet, 10 people shake hands with each other. How many handshakes will there be?
                                        A) 65
                                        B) 100
                                        C) 45
                                        D) 90
                                        ""","""The day after the day after tomorrow is four days before Monday. What day is it today?
                                                A) Tuesday
                                                B) Thursday
                                                C) Monday
                                                D) Saturday
                                                """]
    
    que3 = input(random.choice(third_que))
    print(que3)
    if que3.upper() == "C":
        player_score += 1
    else:
        player_score -= 1

    time.sleep(1)
    print((Fore.MAGENTA + "Processing Answer"))
    time.sleep(1)
    print("_"*60)

    fourth_que = [Fore.YELLOW + """If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?
                    A) 100 minutes
                    B) 5 minutes
                    C) 10 minutes
                    D) 50 minutes
                    ""","""If Sally's daughter is my son's mother, what relation am I to Sally? (I'm male)
                            A) Son
                            B) Son-In-Law
                            C) Brother
                            D) Brother-In-Law
                            ""","""What's the missing letter in this sequence?A - Y - C - W - E - U - G - ?
                                    A) H
                                    B) S
                                    C) A
                                    D) D
                                    """]
    
    que4 = input(random.choice(fourth_que))
    print(que4)
    if que4.upper() == "B":
        player_score += 1
    else:
        player_score -= 1

    time.sleep(1)
    print((Fore.MAGENTA + "Processing Answer"))
    time.sleep(1)
    print("_"*60)

    time.sleep(1)
    print(Fore.RED + "This last question is of Expert Level.")
    print(Fore.RED + "Get Ready.")
    print("_"*60)
    time.sleep(2)

    fifth_que = [Fore.YELLOW + """What Letter comes next?: 
                                  HILT is to LMPY as DENS is to - ?
                                  A) X
                                  B) Y
                                  C) Z
                                  D) W
                                  ""","""Finger is to hand as leaf is to:
                                         A) Twig
                                         B) Branch
                                         C) Root
                                         D) Trunk
                                         ""","""If you rearrange the letters "EADVOBULR" you have something you:
                                                A) Drive On
                                                B) Eat
                                                C) Sleep
                                                D) Exercise
                                                """]
    
    que5 = input(random.choice(fifth_que))
    print(que5)
    if que5.upper() == "A":
        player_score += 1
    else:
        player_score -= 1

    time.sleep(1)
    print((Fore.MAGENTA + "Processing Answer"))
    time.sleep(1)
    print("_"*60)

    time.sleep(1)
    print(Fore.RED + "Here are your results: ")
    time.sleep(3)
    if player_score <= 1:
        print(Fore.CYAN + "Your score: " , player_score)
        time.sleep(1)
        print(Fore.CYAN + "Your IQ is below 30.")
        time.sleep(1)
        print(Fore.CYAN + "Better luck next time.")

    elif player_score > 1 and player_score <= 4:
        print(Fore.CYAN + "Your score: " , player_score)
        time.sleep(1)
        print(Fore.CYAN + "Your IQ is is average 100 to 135.")
        time.sleep(1)
        print(Fore.CYAN + "Try hard to score Full next time.")

    elif player_score == 5:
        print(Fore.CYAN + "Your score: " , player_score)
        time.sleep(1)
        print(Fore.CYAN + "Your IQ is above 160.")
        time.sleep(1)
        print(Fore.CYAN + "Congratulations.")

    ask2 = input("Do you want to retry? ")
    if ask != "yes":
        break

while ask == "no":
    time.sleep(1)
    print(Fore.GREEN + "Ok Then.")
    time.sleep(1)
    print(Fore.GREEN + "Have a good day.")
    print(Fore.MAGENTA + "***")
    break