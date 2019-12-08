# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

import matplotlib

# Section End

# Section: Constants

CURRENTPATH = dirname(abspath(__file__)) + "//books.json"

# Section End

DATASETPATH = "C://Users//howel//Desktop//Book Dataset//"

ratings = pd.read_csv(DATASETPATH + "ratings.csv", names=['user_id', 'book_id', 'rating'])
print(ratings.head())
# to_read = pd.read_csv(DATASETPATH + "to_read.csv")
# print(to_read.columns.values)
books = pd.read_csv(DATASETPATH + "books.csv") # , names=['book_id', 'original_title', 'title'])
print(books.columns.values)
tags = pd.read_csv(DATASETPATH + "tags.csv")
print(tags.head())
book_tags = pd.read_csv(DATASETPATH + "book_tags.csv")
print(book_tags.head())

# books.to_json(path_or_buf=CURRENTPATH, orient="records")
