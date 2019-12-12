# Section: Import modules

import pandas as pd

from os.path import dirname, abspath

import numpy as np

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
                                      columns="bookID",
                                      values="rating").fillna(0)
    # Convert to np array
    npPivot = pivotBooksRatings.as_matrix()

    # Find mean of ratings
    userRatingsMean = np.mean(npPivot, axis=1)

    # De-mean all values in np array
    demeanedPivot = npPivot.reshape(-1,1)

    

def editProfile(userID, books, ratings):
    exit = False
    while not exit:
        print("\n*** User {0} Menu ***".format(userID))
        print("\n** Ratings **")
        userRatings = ratings.loc[ratings["userID"] == userID]
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

        menuChoice = input("\nEnter choice: ")

        if menuChoice == "1" or menuChoice == "2":
            bookID = int(input("Enter book ID: "))
            bookIDsRated = userRatings["bookID"].unique()
            if bookID in bookIDsRated:
                currentRatingRow = ratings.loc[(ratings["userID"] == userID)
                                               & (ratings["bookID"] == bookID)]
                currentRating = currentRatingRow.iloc[0]["rating"]
                print("You rated it {0}/5".format(currentRating))
                rating = int(input("Enter rating (0-5): "))
                ratings.loc[(ratings["userID"] == userID)
                            & (ratings["bookID"] == bookID), "rating"] = rating
            else:
                rating = int(input("Enter rating (0-5): "))
                ratings = ratings.append(pd.DataFrame([[userID,
                                                        bookID,
                                                        rating]],
                                                      columns=["userID",
                                                               "bookID",
                                                               "rating"]),
                                         ignore_index=True)

        elif menuChoice == "3":
            bookID = int(input("Enter book ID: "))
            bookIDsRated = userRatings["bookID"].unique()
            if bookID in bookIDsRated:
                currentRatingRow = ratings.loc[(ratings["userID"] == userID)
                                               & (ratings["bookID"] == bookID)]
                currentRating = currentRatingRow.iloc[0]["rating"]
                print("You rated it {0}/5".format(currentRating))
                confirm = input("Confirm delete by typing 'DEL': ").upper()
                if confirm == "DEL":
                    deleteIndex = ratings[(ratings["userID"] == userID)
                                          & (ratings["bookID"] == bookID)].index
                    ratings.drop(deleteIndex, inplace=True)
            else:
                print("You have not rated this book")
        elif menuChoice == "9":
            exit = True


# Section End

# Section: Main program

getRecommendation(books, ratings)

exit = False
while not exit:
    print("*** Login page ***")
    userID = input("Enter User ID: ")

    # If non valid ID
    if not userID.isdigit():
        continue

    logout = False
    while not logout:
        print("\n*** Main Menu ***")
        print("1. Get recommendation")
        print("2. Edit user profile")
        print("8. Logout")
        print("9. Exit")

        menuChoice = input("\nEnter choice: ")

        if menuChoice == "1":
            getRecommendation(books, ratings)
        elif menuChoice == "2":
            editProfile(int(userID), books, ratings)
        elif menuChoice == "8":
            logout = True
        elif menuChoice == "9":
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
