# From the library random and time, it only imports randint and sleep method.
from random import randint
from time import sleep 

# Start function is the beginning. The other functions are the path the user is directed to depending on their input. Ex: lvlAA is when the user is selects "A" for first other and "A" for second option.

def start(playerName):
    a = "a"
    b = "b"

    print("\n" + playerName + "! Your dad just woke up and you looked out the windows, all of a sudden you see people killing each other and eating brains of other people, those must be zombies!\n")
    sleep(3)
    print("A: Leave in your car!\n \nOR\n \nB: Stay and defend your house!\n")
    while True:
        ans = str.lower(input("Select option 'A' or 'B': "))
        if ans == "a":
            return a
        elif ans == "b":
            return b


def carOrStay():
    a = "a"
    b = "b"

    print("\nIt seems like it was a good choice because your house just got destroyed by the zombies and your dad came with you! However, you do not have unlimited supply of food, water, and gas. What do you want to do?\n")
    sleep(3)
    print("A: Stop at the gas station!\n \nOR\n \nB: Stop at the police station!\n")
    while True:
        ans = str.lower(input("Select option 'A' or 'B': "))
        if ans == "a":
            return a
        elif ans == "b":
            return b


def gasStation():
    random= randint(1,2)
    a1 = "a1"
    a2 = "a2"
    b = "b"

    if random == 1: # 50% chance
        print("\nThe gas station had some food and gas, now what?\n")
        sleep(1)
        print("A: Drive to the airport\n \nOR\n \nB: Stay!\n") 
    if random == 2: # 50% chance
        print("\nThe gas station was destroyed, that was a compelete waste of gas and time and you are out of resources, but there is a helicopter above you\n")
        sleep(3)
        print("A: Stop and try to enter it.\n \nOR\n \nB: Too risky, just run!\n") 
    while True:
        ans = str.lower(input("Select option 'A' or 'B': "))
        if ans == "a" and random == 1:
            return a1
        elif ans == "a" and random == 2:
            return a2
        elif ans == "b":
            return b


def policeStation():
    random= randint(1,2)
    a1 = "a1"
    a2 = "a2"
    b1 = "b1"
    b2 = "b2"

    if random == 1: # 50% chance
        print("\nThe police station had weapons and food, what now?\n")
        sleep(1)
        print("A: Drive to the gas station\n \nOR\n \nB: Drive to the airport\n")
    elif random == 2: # 50% chance
        print("\nThe police station was destroyed, that was a compelete waste of gas and time, but there is a helicopter taking off!\n")
        sleep(2)
        print("A: Try to get in with them\n \nOR\n \nB: Stay\n") 
    while True:
        ans = str.lower(input("Select option 'A' or 'B': "))
        if ans == "a" and random == 1:
            return a1
        elif ans == "a" and random == 2:
            return a2
        elif ans == "b" and random == 1:
            return b1
        elif ans == "b" and random == 2:
            return b2


def airportHeli():
    random= randint(1,10)
    lived = "won"
    dead = "dead"
    if random <=9: # 90% chance
        print("\nA helicopter was there and you made it in time")
        sleep(1)
        return lived
    if random ==10: # 10% chance
        print("\nNo one was there, you ran out of resources and died!")
        sleep(1)
        return dead


def gasOrPoliceHeli():
    random= randint(1,10)
    lived = "won"
    if random <=9: # 90% chance
        print("\nYou and you father made it and and you survived the zombie apocolypse!")
        sleep(2)
        return lived
    elif random == 10: # 10% chance
        print("\nYou made it but a zombie stopped your father from making it, you have escaped the zombie apocolypse!")
        sleep(2)
        return lived


def horde():
    dead = "dead"
    print("\nUnfortunality, a big horde came and you died")
    sleep(1)
    return dead


def leaveOrStay():
    random= randint(1,3)
    dead = "dead"
    a = "a"
    b = "b"

    if random <= 2: # 66.6% chance
        print("\nThere is too many of them, they ended up eating you and your dad alive!")
        sleep(1)
        return dead
    elif random == 3: # 33.3% chance
        print("\nThere are way too many zombies for you to kill, what do you plan on doing?\n") 
        sleep(1)
        print("A: Leave in your car!\n \nOR\n \nB: Keep defending!\n")
    while True:
        ans = str.lower(input("Select option 'A' or 'B': "))
        if ans == "a":
            return a
        elif ans == "b":
            return b


def stayedTooLong():
    dead = "dead"
    print("\nThere is too many of them, they ended up eating you and your dad alive!")
    sleep(1)
    return dead


# Some comments could be wrong
def main():
    replay = "yes"
    while replay == "yes" or replay == "ye" or replay == "y":
        a = start(input("\nHello, what is your name?: "))
        if a == "a":
            a = carOrStay() # A
            if a == "a":
                a = gasStation() # AA
                if a == "a1":
                    a = airportHeli() # AAAA1
                    if a == "dead":
                        replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                    elif a == "won":
                        replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                elif a == "a2":
                    a = gasOrPoliceHeli() # AAAA2
                    if a == "won":
                        replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                elif a == "b":
                    a = horde() # AAB
                    if a == "dead":
                        replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))

            elif a == "b":
                a = policeStation() # AB
                if a == "a1":
                    a = gasStation() # ABA1
                    if a == "a1":
                        a = airportHeli() # ABAA1
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                        elif a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                    elif a == "a2":
                        a = gasOrPoliceHeli() # ABAA2
                        if a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                    elif a == "b":
                        a = horde() # ABB2
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                elif a == "a2":
                    a = airportHeli() # ABA2
                    if a == "dead":
                        replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                    elif a == "won":
                        replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                elif a == "b1":
                    a = airportHeli() # ABB1
                    if a == "dead":
                        replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                    elif a == "won":
                        replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                elif a == "b2":
                    a = horde() # ABB2
                    if a == "dead":
                        replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))


        elif a == "b": # B
            a = leaveOrStay()
            if a == "dead":
                replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
            elif a == "a":
                a = carOrStay() # BA
                if a == "a":
                    a = gasStation() #BAA
                    if a == "a1":
                        a = airportHeli() # BAA1
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                        elif a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                    elif a == "a2":
                        a = gasOrPoliceHeli() # BAA2
                        if a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                elif a == "b":
                    a = policeStation() # BAB
                    if a == "a1":
                        a = gasStation() # BABA1
                        if a == "a1":
                            a = airportHeli() # BABAA1
                            if a == "dead":
                                replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                            elif a == "won":
                                replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                        elif a == "a2":
                            a = gasOrPoliceHeli() # BABAA2
                            if a == "won":
                                replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                        elif a == "b":
                            a = horde() # BABAB
                            if a == "dead":
                                replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                    elif a == "a2":
                        a = airportHeli() # BABA2
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                        elif a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                    elif a == "b1":
                        a = airportHeli() # BABB1
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                        elif a == "won":
                            replay = str.lower(input("\nThere are multiple way to win, do you want to play again? (Yes or No?): "))
                    elif a == "b2":
                        a = horde() # BABB2
                        if a == "dead":
                            replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))
                        
            elif a == "b": # BB
                a = stayedTooLong()
                if a == "dead":
                    replay = str.lower(input("\nDo you want to play again? (Yes or No?): "))

    print("\nThanks for playing!\n") # Executed when the loop is broken
    
main()