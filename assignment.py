# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End

# Section: Constants

PATH = dirname(abspath(__file__)) + "//"

BOOKSPATH = PATH + "books.json"
RATINGSPATH = PATH + "ratings.json"
USERSPATH = PATH + "users.json"

# Section End

# Section: Load database

books = pd.read_json(path_or_buf=BOOKSPATH, orient='records')

ratings = pd.read_json(path_or_buf=RATINGSPATH, orient='records')
if len(ratings.columns.values) == 0:
    userIDs = []
    bookIDs = []
    bookRatings = []
    ratings = pd.DataFrame(data={"userID": userIDs, "bookID": bookIDs,
                                 "bookRating": bookRatings})

users = pd.read_json(path_or_buf=USERSPATH, orient='records')
if len(users.columns.values) == 0:
    userIDs = []
    bookIDs = []
    bookRatings = []
    users = pd.DataFrame(data={"userID": userIDs, "bookID": bookIDs,
                               "bookRating": bookRatings})

# Section End

print(books)
print(ratings)
print(users)

# Section: Save database

books.to_json(path_or_buf=BOOKSPATH, orient='records')
ratings.to_json(path_or_buf=RATINGSPATH, orient='records')
users.to_json(path_or_buf=USERSPATH, orient='records')

# Section End
