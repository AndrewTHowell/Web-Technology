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

print(books)
print(ratings)

# Section: Save database

ratings.to_csv(CURRENTPATH+"//ratings.csv")

# Section End
