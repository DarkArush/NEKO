name = input("What is the name of the item you sold?")
cp = int(input("How much did you paid to buy it?"))
sp = int(input("And in how much did you sell it?"))

a = sp-cp
b = cp-sp

if sp>cp and a <= 20:
    print("Well it's a profit, but not much.")
    e = input("Do you want to know the secret by which you can earn more profit?(Yes or No)")
    if e.lower() == "yes" or e == "Yes":
        print("Ok so here's the secret.")
        print("Work Hard You Dumb Piece Of Shit!")
    elif e.lower() == "no" or e == "No":
        print("Ok Then! Stay Happy with your Meagre Earnings you Pig!")

elif sp>cp and a >= 200:
    print("Well it's a good profit! Congratulations!")
    e = input("But, do you want to know the secret by which you can earn more profit?(Yes or No)")
    if e.lower() == "yes" or e == "Yes":
        print("Ok so here's the secret.")
        print("Work Hard More You Dumb Piece Of Shit!")
    elif e.lower() == "no" or e == "No":
        print("Ok Then! Stay Happy with your Shitty Earnings you PoopHead!")

elif cp>sp and b <= 20:
    print("It's a loss you Dumb! But it's good that it's not much.")
    e = input("Do you want to know the secret by which you can turn this loss into profit?(Yes or No)")
    if e.lower() == "yes" or e == "Yes":
        print("Ok so here's the secret.")
        print("Work Hard You Dumb Piece Of Shit!")
    elif e.lower() == "no" or e == "No":
        print("Ok Then! Go to H*ll with the Debt you just Possessed you Pig!")

elif cp>sp and b >= 200:
    print("It's a Frickin big loss! What are you doing you Rotten Peanuts!")
    e = input("Do you want to know the secret by which you can turn this loss into profit?(Yes or No)")
    if e.lower() == "yes" or e == "Yes":
        print("Ok so here's the secret.")
        print("Work Hard You Dumb Piece Of Shit!")
    elif e.lower() == "no" or e == "No":
        print("Ok Then! Go to H*ll with the Debt you just Possessed you Pig!")

elif cp == sp:
    print("What Da Hail!! No profit you DipShit.")
    e = input("Do you want to know the secret by which you can make Profit?(Yes or No)")
    if e.lower() == "yes" or e == "Yes":
        print("Ok so here's the secret.")
        print("Work Hard You Dumb Piece Of Shit!")
    elif e.lower() == "no" or e == "No":
        print("Ok Then! Just be Poor and Homeless with this Business you Pig!")

else:
    print("I Don't Know What to Say to you.")
    print("Get out from the House! You Are Adopted.")
