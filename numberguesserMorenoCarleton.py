#Martha Moreno Gonzalez and Jadan Carleton
#Friday, February 21st, 2025

#This program allows the user to try and guess a number between 0 and 10
#and gives hints if their guess should be higher or lower.

import random

counter = True

while counter == True:

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

    

    keepPlaying = input("Would you like to guess another number (Y/N)?")
    if keepPlaying == "Y":
        counter = True
    elif keepPlaying == "N":
        counter = False  
    else:
        counter = False

print("Thank you for playing!")
