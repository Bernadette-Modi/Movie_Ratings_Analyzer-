#Movie Ratings Analyzer
from array import *
ratings = array.array('i', [3, 5, 4, 2, 5, 1, 4])
average_rating = sum(ratings) / len(ratings)
highest_rating = max(ratings)
lowest_rating = min(ratings)
