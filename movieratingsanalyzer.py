#Movie Ratings Analyzer
from array import *
movie = input("Enter the movie title: ")
rate = (input("Enter movie ratings (1-5) separated by spaces: ")).split()

ratings = array('i', [])
print("🎬 Movie Rating System 🎬")
print("Enter ratings from 1 to 5. Type 'over' to stop.")

while True:
    movie = input("Enter the movie you want to rate: ")
    rate = input("Enter a rating (1-5) or 'over' to finish: ")
    if rate.lower() == 'over':
        break 
    

average_rating = sum(ratings) / len(ratings)
highest_rating = max(ratings)
lowest_rating = min(ratings)
rating_counts = {i: ratings.count(i) for i in range(1,6)}

#Print statements
print(f"Average Rating: {average_rating:.2f}")
print(f"Highest Rating: {highest_rating}")
print(f"Lowest Rating: {lowest_rating}")
print(f"Rating Count for the movie {movie}: ")
for rating, count in rating_counts.items():
    print(f"{rating}⭐: {count} time(s)")