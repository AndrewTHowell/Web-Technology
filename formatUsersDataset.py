# Section: Import modules

import json

import pandas as pd

from os.path import dirname, abspath

# Section End

userIDs = []
bookIDs = []
bookRatings = []

ratings = pd.DataFrame(data={"userID": userIDs, "bookID": bookIDs,
                             "bookRating": bookRatings})

currentPath = dirname(abspath(__file__)) + "//ratings.json"
ratings.to_json(path_or_buf=currentPath, orient='records')
