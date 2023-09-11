x = int(input("Enter A Number: "))
y = int(input("Enter Another Number: "))
print("The List is:", x, y)

c = input("Do you want to Swap the Numbers in the List?(Yes or No)")

if c.lower() == "yes" or c == "Yes":
    temp = x
    x = y
    y = temp
    print("The List After the Changes: {}".format(x), format(y))

elif c.lower() == "no" or c == "No":
    print("Ok! The List is:", x, y)

else:
    print("Sorry but your Answer has to be in Either Yes or No")

