#Martha Moreno Gonzalez and Jadan Carleton
#Friday, February 21st, 2025

#This program allows the user to try and guess a number between 0 and 10
#and gives hints if their guess should be higher or lower.

import random

answer = random.randrange(1,11)

guess = int(input("Please guess a number between 1 and 10: "))

for i in range(100):
        
if guess == 0:
    print("Process finished with exit code 0")
    break
elif guess == answer:
        print("Well done, you guessed it!")
        break
elif guess > answer:
            print("Lower")
else:
            print("Higher")

    guess = int(input("Please guess again: "))


print("Thank you for playing!")
