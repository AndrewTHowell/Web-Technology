# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End

# Section: Constants

PATH = dirname(abspath(__file__)) + "//"

# Section End

# Section: Load database

booksPath = PATH + "books.json"
books = pd.read_json(path_or_buf=booksPath, orient='records')

# Section End

print(books)
