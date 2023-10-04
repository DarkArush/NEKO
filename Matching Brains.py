import random

print("Does our mind think the same?")
print("Let's find out!")

lisp = input("""Choose a word from this list:
                1. Love
                2. Hate
                3. Anger
                4. Happy
                5. Sad
                Choose the word: """)

valid_lisp = ["love", "hate", "anger", "happy", "sad"]

if lisp in valid_lisp:
    computer_lisp = random.choice(valid_lisp)
    print(computer_lisp)

    if lisp != computer_lisp:
        print("Our choices don't match")
    else:
        print("Wow! Our choices do really match.")
