# from the library random and time, it only imports randint and sleep method.
from random import randint
from time import sleep # not yet used


def levelOne(playerName):
    print("\n" + playerName + "! Your dad just woke up and you looked out the windows, all of a sudden you see people killing each other and eating brains of other people, those must be zombies!")
    print("What do you want to do?\n \nA: Grab your pistol, 4 canned beans, 4 water bottles, and leave in your car!\n \nOR\n \nB: Stay and defend your house!")


def levelTwo(optionPicked):
    randomoptionPicked = randint(1,2)
    a1 = "a1"
    b2 = "b2"
    dead = "True"
    while optionPicked != "a" or optionPicked != "b":
        if optionPicked == "a": # 100% chance
            print("\nIt seems like it was a good choice because your house just got destroyed by the zombies and your dad came with you! However, you do not have unlimited supply of food, water, and gas. What do you want to do?\n \nA: Stop at the gas station!\n \nOR\n \nB: Stop at the police station!\n")
            return a1

        elif optionPicked == "b" and randomoptionPicked == 2: # 50% chance
            print("There is too many of them, they ended up eating you and your dad alive!")
            return dead
        elif optionPicked == "b" and randomoptionPicked == 1: # 50% chance
            print("\nThere are way too many zombies for you to kill, what do you plan on doing?\n \nA: Rush to your car!\n \nOR\n \nB: Keep defending!")
            return b2
        else:
            optionPicked = str.lower(input())


def levelThreeA(optionPicked):
    randomoptionPicked= randint(1,4)
    dead = "True"
    lived = "won"
    while optionPicked != "a" or optionPicked != "b":
        if optionPicked == "a" and randomoptionPicked <= 2: # 50% chance
            print("The gas station had some food and gas, what now?") # I'm aware the options are not given
            break
        elif optionPicked == "a" and randomoptionPicked >= 3: # 50% chance
            print("The gas station was destroyed, that was a compelete waste of gas and time.") # I'm aware the options are not given
            break
            
        elif optionPicked == "b" and randomoptionPicked <= 2: # 75% chance
            print("The police station had weapons and food, what now?") 
            break
        elif optionPicked == "b" and randomoptionPicked >= 3: # 25% chance
            print("The police station was destroyed, that was a compelete waste of gas and time.") 
            break
        else:
            optionPicked = str.lower(input())
    

def levelThreeB(optionPicked):
    randomoptionPicked= randint(1,4)
    dead = "True"
    lived = "won"
    while optionPicked != "a" or optionPicked != "b":
        if optionPicked == "a" and randomoptionPicked <= 2: # 50% chance
            print("The gas station had some food and gas, what now?") # I'm aware the options are not given
            break
        elif optionPicked == "a" and randomoptionPicked >= 3: # 50% chance
            print("The gas station was destroyed, that was a compelete waste of gas and time.") # I'm aware the options are not given
            break
            
        elif optionPicked == "b" and randomoptionPicked != 4: # 75% chance
            print("There is too many of them, you ran out of resources and they ate you alive!") 
            return dead
        elif optionPicked == "b" and randomoptionPicked == 4: # 25% chance
            print("Luckily, a helicopter came to the rescue, you survived the zombie apocalypse!") 
            return lived
        else:
            optionPicked = str.lower(input())


# Not a real level...
def levelFour(optionPicked):
    print("Testing if it made it this far") 


# The input in the arguments are compared with the function's variable in the parameter. And the levels are in a while loop until the loop is broken by the player not inputting "yes" for variable "replay"
def main():
    replay = "yes"
    while replay == "yes" or replay == "y":
        levelOne(input("Hello, what is your name? ")) # Executes input then the function
        b = levelTwo(str.lower(input())) # Executes input then the function
        if b == "True":
            replay = str.lower(input("Do you want to play again? (Yes or No?) "))
        elif c == "won":
            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?) "))
        elif b == "a1":
            c = levelThreeA(str.lower(input()))
            d = levelFour("car")
            if c == "True":
                replay = str.lower(input("\nDo you want to play again? (Yes or No?) "))
            elif c == "won":
                replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?) "))
            else:
                replay = str.lower(input("\nDo you want to play again? (Yes or No?) "))
        else: 
            if b == "b2":
                c = levelThreeB(str.lower(input()))
                d = levelFour("car")
            elif c == "True":
                replay = str.lower(input("\nDo you want to play again? (Yes or No?) "))
            elif c == "won":
                replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?) "))
            else:
                replay = str.lower(input("\nDo you want to play again? (Yes or No?) "))



    print ("Thanks for playing!")

main()