# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End

# Section: Constants

PATH = dirname(abspath(__file__)) + "//"

BOOKSPATH = PATH + "books.csv"

# Section End

# Section: Load database

books = pd.read_csv(CURRENTPATH+"//books.csv")
ratings = pd.read_csv(CURRENTPATH+"//ratings.csv")

# Section End

print(books)
print(ratings)
print(users)

# Section: Save database

books.to_json(path_or_buf=BOOKSPATH, orient='records')
ratings.to_json(path_or_buf=RATINGSPATH, orient='records')
users.to_json(path_or_buf=USERSPATH, orient='records')

# Section End
