# For loop checks every item in first inventory and compares it with the second iventory. If there is a duplicate, it will return the item in the list that is found in both inventories, if not, it will return nothing aka "None" in the output
def lists(inventory1, inventory2):
    print("1. " + str(inventory1), "\n2. " + str(inventory2))

    for items in inventory1:
        if items in inventory2:
            return items
        else:
            return 

# Only sword is duplicated.
def main():
    a = lists(["sword", "hammer", "shield"], ["candy", "sword", "chocolate"]) # Assigns a list to these 2 inventories for the lists function.
    print(a)
main()