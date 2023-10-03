import random
import math

x = random.randint(1, 100)
print("\n\tYou've only ",
	round(math.log(99 + 1, 2)),
	" chances to guess the integer!\n")

count = 0

while count < math.log(99 + 1, 2):
	count += 1

	guess = int(input("Guess a number between 1 to 100: "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(99 + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

