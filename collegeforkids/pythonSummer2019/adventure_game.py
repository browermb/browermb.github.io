print("Welcome to ZORK")
print("WEST OF HOUSE")
print("There is an open field west of a white house, with a board front door.")
print("There is a small mailbox here.")
print("A rubber mat saying 'Welcome to Zork!' lies by the door")
response = input("What direciton would you like to go ")
if response == "North":
    print("You are facing the north side of a white house. \n There is no door here, and all the windows are barred.")
elif response == "South":
    print("You are facing the north side of a white house. \n There is no door here, and all the windows are barred.")
elif response == "East":
    print("The door is locked and there is no key.")
elif response == "West":
    print("This is a forest, with trees in directions around you.")