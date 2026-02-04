# Number Guessing Game

import random
print("Welcome to Number Guessing Game")
num = random.randint(1,20)
guess = 0
attempt = 0
while guess != num:
    guess = int(input("Enter the guessing number(1-20):"))
    attempt += 1
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        print(f"Congrats! You guessed it in {attempt} attempt.")
