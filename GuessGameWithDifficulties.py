# This is a Guess the Number Game, With Difficulties
import random

guessesTaken = 0

myName = input("Hello! What is your name: ")

print("Select difficulty: Easy, Medium, or Hard?")
response = False

# Loop until a difficulty is selected
while response == False:
    difficulty = str.lower(input())
    if difficulty == "easy":
        number = random.randint(1, 20)
        print("Well, " + myName + ", I am thinking of a number between 1 and 20. You have 5 guesses!")
        break
    
    elif difficulty == "medium":
        number = random.randint(1, 30)
        print("Well, " + myName + ", I am thinking of a number between 1 and 30. You have 5 guesses!")
        break
            
    elif difficulty == "hard":
        number = random.randint(1, 50)
        print("Well, " + myName + ", I am thinking of a number between 1 and 50. You have 5 guesses!")
        break
    
    else:
        print("I didn't get that, please enter the difficulty again")


for guessesTaken in range(5):
    print("Take a guess.") # Four spaces in front of "print".
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.") # Eight spaces in front of "print"

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

   
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")