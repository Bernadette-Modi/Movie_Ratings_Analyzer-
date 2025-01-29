#Movie Ratings Analyzer
from array import *
movie = input("Enter the movie title: ")
rate = (input("Enter movie ratings (1-5) separated by spaces: ")).split()

ratings = array('i', [int(num) for num in rate])
average_rating = sum(ratings) / len(ratings)
highest_rating = max(ratings)
lowest_rating = min(ratings)
rating_counts = {i: ratings.count(i) for i in range(1,6)}


print(f"Average Rating: {average_rating:.2f}")
print(f"Highest Rating: {highest_rating}")
print(f"Lowest Rating: {lowest_rating}")
print(f"Rating Count for the movie {movie}: ")
for rating, count in rating_counts.items():
    print(f"⭐{rating} stars: {count} time(s)")