x = input("""Here is a list of some 2D shapes:1. Rectangle
                                 2. Square
                                 3. Triangle
                                 4. Circle
Select the Number of the Shape you want to calculate the area of: """)

if x == "1":
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    ar_rec = l*b
    print("The Area is:", ar_rec, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = ar_rec*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", ar_rec, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "2":
    s = int(input("Enter Length of the Side: "))
    ar_sq = s*s
    print("The Area is:", ar_sq, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = ar_sq*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", ar_sq, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "3":
    b = int(input("Enter Length of the Base: "))
    h = int(input("Enter Height: "))
    ar_triangle = 0.5*b*h
    print("The Area is:", ar_triangle, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = ar_triangle*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", ar_triangle, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "4":
    r = int(input("Enter Radius: "))
    pie = 22/7
    ar_circle = pie*r*r
    print("The Area is:", ar_circle, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = ar_circle*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", ar_circle, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

else:
    print("Sorry! There is no such 2D Shape in our List called", x, ".")
