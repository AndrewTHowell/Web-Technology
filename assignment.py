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
ratings = pd.read_csv(CURRENTPATH+"//ratings.csv")

# print(books)
# print(ratings)

# Section End

# Section: Functions


def getRecommendation(books, ratings):
    pivotBooksRatings = ratings.pivot(index="userID",
                                      columns="bookIDs",
                                      values="ratings")
    print(pivotBooksRatings.head())


def editProfile(userID, books, ratings):
    exit = False
    while not exit:
        print("\n*** User {0} Menu ***".format(userID))
        print("\n** Ratings **")
        userRatings = ratings.loc[ratings['userID'] == userID]
        for index, rating in userRatings.iterrows():
            bookRow = books.loc[rating["bookID"]]
            bookID = bookRow["bookID"]
            bookTitle = bookRow["bookTitle"]
            rating = rating["rating"]
            print("Book ID: {0}, Book Title: {1}, Your rating: {2}"
                   .format(bookID, bookTitle, rating))
        print("\n** Options **")
        print("1. Add book rating")
        print("2. Edit book rating")
        print("3. Delete book rating")
        print("9. Return to Main Menu")

        menuChoice = int(input("\nEnter choice: "))
        if menuChoice == 1:
            bookID = int(input("Enter book ID: "))
            print("userRatings['bookID'] unique: {0}".format(userRatings["bookID"].unique()))
            if bookID in userRatings["bookID"].unique():
                print("Replace")
        elif menuChoice == 2:
            bookID = int(input("Enter book ID: "))
            rating = ratings.loc[(ratings['userID'] == userID)
                                 & ratings['bookID'] == bookID]["rating"]
        elif menuChoice == 3:
            bookID = int(input("Enter book ID: "))
        elif menuChoice == 9:
            exit = True

# Section End

# Section: Main program

exit = False
while not exit:
    print("*** Login page ***")
    userID = int(input("Enter User ID: "))

    logout = False
    while not logout:
        print("\n*** Main Menu ***")
        print("1. Get recommendation")
        print("2. Edit user profile")
        print("8. Logout")
        print("9. Exit")

        menuChoice = int(input("\nEnter choice: "))
        if menuChoice == 1:
            getRecommendation(books, ratings)
        elif menuChoice == 2:
            editProfile(userID, books, ratings)
        elif menuChoice == 8:
            logout = True
        elif menuChoice == 9:
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
