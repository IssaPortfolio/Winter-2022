def game([playerInfo]):

    playerInfo[0,1] = 7
    return playerInfo


    

def main():
    a = game([["survivors", 1], ["weapons", 3], ["cars", 2]])
    print(a)

main()