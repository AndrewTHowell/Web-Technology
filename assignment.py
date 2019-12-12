# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End

# Section: Constants

CURRENTPATH = dirname(abspath(__file__))

# Section End

# Section: Load database

books = pd.read_csv(CURRENTPATH+"//books.csv")
ratings = pd.read_csv(CURRENTPATH+"//ratings.csv", index_col=0)

# Section End

# Section: Functions


# Section End

# Section: Main program

exit = False
while not exit:
    print("*** User Menu ***")
    userID = int(input("Enter User ID: "))

    logout = False
    while not logout:
        print("\n*** User {0}: Menu ***".format(userID))
        print("1. Do stuff")
        print("8. Logout")
        print("9. Exit")

        menuChoice = int(input("\nEnter choice: "))
        if menuChoice == 8:
            logout = True
        if menuChoice == 9:
            logout = True
            exit = True

    if exit:
        break

    choice = input("\nExit or Log in? (E or L): ").upper()
    if choice == "E":
        exit = True
    else:
        print("\n")

# Section End

# Section: Save database

ratings.to_csv(CURRENTPATH+"//ratings.csv")

# Section End
