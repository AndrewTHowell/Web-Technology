# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End


bookIDCounter = 0
bookIDs = []
bookTitles = []
authors = []
genres = []

dataset = "C://Users//howel//Desktop//booksummaries//booksummaries.txt"
with open(dataset, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        [_, _, bookTitle, _, _, genre, _] = line.split("\t")

        if genre != "":
            genre = list(json.loads(genre).values())
        else:
            genre = []

        bookIDs.append(bookIDCounter)
        bookTitles.append(bookTitle)
        genres.append(genre)

        bookIDCounter += 1

books = pd.DataFrame(data={"bookID": bookIDs, "bookTitle": bookTitles,
                           "bookGenres": genres})


userIDs = []
bookIDs = []
bookRatings = []

ratings = pd.DataFrame(data={"userID": userIDs, "bookID": bookIDs,
                             "bookRating": bookRatings})

currentPath = dirname(abspath(__file__)) + "//ratings.json"
ratings.to_json(path_or_buf=currentPath, orient='records')

print(books)

currentPath = dirname(abspath(__file__)) + "//books.json"
books.to_json(path_or_buf=currentPath, orient='records')
