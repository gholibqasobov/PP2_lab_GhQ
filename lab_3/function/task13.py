from random import randint

interval = randint(1, 20)

name = input("Hello! What is your name? \n")

print("Well, " + str(name) + ", I am thinking of a number between 1 and 20. ")
n = None
# n = input("Take a guess. "))
count = 0
while n != interval:
    n = int(input("Take a guess. \n"))
    if n < interval:
        print("Your guess is too low.")
    elif n > interval:
        print("Your guess is too high.")

    count += 1
else:
    print("Good job, " + str(name) + "! You guessed my number in " + str(count) + " guesses!")
