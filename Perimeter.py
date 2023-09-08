x = input("""Here is a list of some 2D shapes:1. Rectangle
                                 2. Square
                                 3. Triangle
                                 4. Circle
Select the Number of the Shape you want to calculate the perimeter of: """)

if x == "1":
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    per_rec = 2*(l+b)
    print("The Area is:", per_rec, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = per_rec*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", per_rec, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "2":
    s = int(input("Enter Length of the Side: "))
    per_sq = 4*s
    print("The Area is:", per_sq, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = per_sq*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", per_sq, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "3":
    t = input("""There are Three types of Triangles: 1. Equilateral Triangle
                                    2. Isosceles Triangle
                                    3. Scalene Triangle
                  Choose the type of Triangle you want to find the perimeter of by putting the Numbers:""")
    if t == "1":
        s = int(input("""In a Equilateral Triangle, all the Three sides are equal.
                         Therefore, Enter the Length of the Side: """))
        per_triangle = s+s+s
        print("The perimeter is", per_triangle, "cm.")
        u = input("""Do you want your answer to be in metres? 
                         Type 1. For Yes
                         Type 2. For No
                         Type your answer here: """)
        if u == "1":
            m = per_triangle * 100
            print("Ok Then! The Answer is", m, "m.")
        elif u == "2":
            print("Ok Then! Your Final Answer is", per_triangle, "cm.")
        else:
            print("Sorry! We can't give you the answer in this unit:", u, ".")
    elif t == "2":
        s_one = int(input("""In a Isosceles Triangle, Two sides are equal and one Side is unequal.
                         Therefore, Enter the Length of the equal Side and: """))
        s_two = int(input("Enter the Length of the unequal Side: "))
        per_triangle = s_one + s_one + s_two
        print("The perimeter is", per_triangle, "cm.")
        u = input("""Do you want your answer to be in metres? 
                     Type 1. For Yes
                     Type 2. For No
                     Type your answer here: """)
        if u == "1":
            m = per_triangle * 100
            print("Ok Then! The Answer is", m, "m.")
        elif u == "2":
            print("Ok Then! Your Final Answer is", per_triangle, "cm.")
        else:
            print("Sorry! We can't give you the answer in this unit:", u, ".")
    elif t == "3":
        s_one = int(input("""In a Scalene Triangle, all the Three sides are unequal.
                         Therefore, Enter the Length of the first Side : """))
        s_two = int(input("Enter the Length of the second Side: "))
        s_three = int(input("Enter the Length of the third Side: "))
        per_triangle = s_one + s_two + s_three
        print("The perimeter is", per_triangle, "cm.")
        u = input("""Do you want your answer to be in metres? 
                     Type 1. For Yes
                     Type 2. For No
                     Type your answer here: """)
        if u == "1":
            m = per_triangle*100
            print("Ok Then! The Answer is", m, "m.")
        elif u == "2":
            print("Ok Then! Your Final Answer is", per_triangle, "cm.")
        else:
            print("Sorry! We can't give you the answer in this unit:", u, ".")

elif x == "4":
    r = int(input("Enter Radius: "))
    pie = 22/7
    per_circle = 2*pie*r
    print("The Area is:", per_circle, "cm.")
    u = input("""Do you want your answer to be in metres? 
                 Type 1. For Yes
                 Type 2. For No
                 Type your answer here: """)
    if u == "1":
        m = per_circle*100
        print("Ok Then! The Answer is", m, "m.")
    elif u == "2":
        print("Ok Then! Your Final Answer is", per_circle, "cm.")
    else:
        print("Sorry! We can't give you the answer in this unit:", u, ".")

else:
    print("Sorry! There is no such 2D Shape in our List called", x, ".")
