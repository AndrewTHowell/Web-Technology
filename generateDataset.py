import pandas as pd

from os.path import dirname, abspath

import random

CURRENTPATH = dirname(abspath(__file__))

books = pd.read_csv(CURRENTPATH+"//books.csv")

userIDs = []
bookIDs = []
ratings = []

# Generate 10 random users
for user in range(10):
    numberOfBooks = books.shape[0]
    print("numberOfBooks: {0}".format(numberOfBooks))
    potentialBooksLength = random.randrange(0, numberOfBooks//2)
    print("potentialBooksLength: {0}".format(potentialBooksLength))
    potentialBooks = random.sample(range(numberOfBooks), potentialBooksLength)
    print("potentialBooks: {0}".format(potentialBooks))
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
