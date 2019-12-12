import pandas as pd

from os.path import dirname, abspath

from random import random

CURRENTPATH = dirname(abspath(__file__))

books = pd.read_csv(CURRENTPATH+"//books.csv")
ratings = pd.read_csv(CURRENTPATH+"//ratings.csv")

# Generate 10 random users
for in range(10):
    numberOfBooks = rat

ratings.to_csv(CURRENTPATH+"//ratings.csv")
