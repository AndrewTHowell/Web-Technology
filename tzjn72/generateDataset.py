import pandas as pd

from os.path import dirname, abspath

import random

CURRENTPATH = dirname(abspath(__file__))

books = pd.read_csv(CURRENTPATH+"//books.csv")

userIDs = []
bookIDs = []
ratings = []

# Generate 20 random users
for user in range(20):
    numberOfBooks = books.shape[0]

    potentialBooksLength = random.randrange(0, numberOfBooks)

    potentialBooks = random.sample(range(numberOfBooks), potentialBooksLength)

    for bookID in potentialBooks:
        # Random as to whether this book is reviewed
        if bool(random.getrandbits(1)):
            rating = random.randint(0, 5)
            userIDs.append(user)
            bookIDs.append(bookID)
            ratings.append(rating)

ratings = pd.DataFrame(data={"userID": userIDs, "bookID": bookIDs,
                             "rating": ratings})

ratings.to_csv(CURRENTPATH+"//ratings.csv")
