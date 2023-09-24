x = int(input("Enter A Number: "))
y = int(input("Enter Another Number: "))
z = int(input("Enter One More Number: "))
print("The List is:",x, y, z)

c = input("Do you want to Swap the Numbers in the List?(Yes or No)")

if c.lower() == "yes" or c == "Yes":
    s = int(input("""There are 5 Ways in which you can Swap the Numbers:
                     1. Change the Second No. to First, Third No. to Second and First No. to Third.
                     2. Change the First No. to Second, Third No. to First and Second No. to Third.
                     3. Let the First No. be First, Change Third No. to Second and Second No. to Third.
                     4. Change the First No. to Third, Let Second No. be Second and Third No. to First.
                     5. Change the First No. to Second, Second No. to First and Let Third No. be Third.
                     Choose any Way by just Simply Entering the Number Here: """))
    if s == 1:
        temp = x
        x = y
        y = temp
        y = z
        z = temp
        print("The List After the Changes: {}".format(x), format(y), format(z))
    elif s == 2:
        temp = y
        y = x
        x = temp
        x = z
        z = temp
        print("The List After the Changes: {}".format(x), format(y), format(z))
    elif s == 3:
        temp = y
        y = z
        z = temp
        print("The List After the Changes: {}".format(x), format(y), format(z))
    elif s == 4:
        temp = x
        x = z
        z = temp
        print("The List After the Changes: {}".format(x), format(y), format(z))
    elif s == 5:
        temp = x
        x = y
        y = temp
        print("The List After the Changes: {}".format(x), format(y), format(z))
    else:
        print("Your Choice Should be in Numbers. Please try again.")

elif c.lower() == "no" or c == "No":
    print("Ok! The List is:", x, y, z)

else:
    print("Sorry but your Answer has to be in Either Yes or No")

