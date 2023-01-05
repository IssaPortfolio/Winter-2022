import time

# First joke
print("What do you get when you cross a snowman with a vampire?")
joke1 = str.lower(input())
time.sleep(0.5)
if joke1 == "frostbite!" or joke1 == "frostbite":
    print("Correct!")
else:
    print("Frostbite!")


# Second joke
print()
print()
print("What do dentists call an astronaut's cavity?")
joke2 = str.lower(input())
time.sleep(0.5)
if joke2 == "a black hole!" or joke2 == "a black hole":
    print("Correct!")
else:
    print("A black hole!")


# Third joke
# I don't understand this knock knock joke but this is a loop until the user inputs "who's there?" or "who's there" or "who is there?" or "who is there" to breaks the loop.
print()
print()
print("Knock knock.")
knockKnock = True
while knockKnock == True:
    joke3a = str.lower(input())
    time.sleep(0.5)
    print()
    if joke3a == "who's there?" or joke3a == "who's there" or joke3a == "who is there?" or joke3a == "who is there":
        print("Interrupting cow.")
        joke3b = input()
        print()
        print('Interrupting cow wh', end='')
        print('-MOO!')
        break
    else:
        print("Knock knock.")